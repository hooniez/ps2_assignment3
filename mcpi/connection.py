import socket
import select
import sys
from .util import flatten_parameters_to_bytestring

import base64
# import for key exchange
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from cryptography.fernet import Fernet

""" @author: Aron Nieminen, Mojang AB"""

class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.shared_key = None
        self.lastSent = ""

    def get_shared_key(self):
        # Generate some parameters. These can be reused.
        parameters = dh.generate_parameters(generator=2, key_size=2048)
        # Generate a private key for use in the exchange.
        p = parameters.parameter_numbers().p # The prime modulus value
        g = parameters.parameter_numbers().g # The generator value (must be 2 or greater)
        a_private_key = parameters.generate_private_key() # Client secret key
        a = a_private_key.private_numbers().x # Client secret number
        g_pow_a_mod_p = a_private_key.public_key().public_numbers().y # Client public number
        data = (p, g, g_pow_a_mod_p)

        b = int(self.sendReceive(b"dh_key_exchange", data)) # Server public value

        shared_key = pow(b, a, p)

        # SHA256 to make the length of the shared key most optimal
        digest = hashes.Hash(hashes.SHA256())
        digest.update(str(shared_key).encode())
        symmetric_key = digest.finalize()

        self.shared_key = base64.urlsafe_b64encode(symmetric_key)

        

        # server_msg = self.sendReceive(b"chat.post", "hello")
        # print(server_msg)

        # self.sendReceiveDH(b"client_key_exchange", g_pow_a_mod_p)

        # # Reduce the length of the shared key from DH using SHA-256
        

        # # print("Shared_key_bytes are" + str(symmetric_key))

        

        


        return self.shared_key


    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  "Drained Data: <%s>\n"%data.strip()
            e += "Last Message: <%s>\n"%self.lastSent.strip()
            sys.stderr.write(e)

    def sendEncrypted(self, f, *data):
        """
        Sends data. Note that a trailing newline '\n' is added here

        The protocol uses CP437 encoding - https://en.wikipedia.org/wiki/Code_page_437
        which is mildly distressing as it can't encode all of Unicode.
        """
        # Use the shared key from DH hasehd with SHA-256 to encrypt a message

        

        s = b"".join([f, b"(", flatten_parameters_to_bytestring(data), b")", b"39490830", b"\n"])

        f = Fernet(self.shared_key)
        token = f.encrypt(s)

        self._send(token)

    def _send(self, s):
        """
        The actual socket interaction from self.send, extracted for easier mocking
        and testing
        """
        self.drain()
        self.lastSent = s

        self.socket.sendall(s)

    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError("%s failed"%self.lastSent.strip())
        return s

    def receiveEncryptedMsg(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        self.socket.settimeout(50)
        print(self.socket.recv(4096))

    def sendReceiveEncrypted(self, f, *data):
        """Sends and receive data"""
        self.sendEncrypted(f, *data)
        return self.receive()

    def send(self, f, *data):
         """
         Establishes a TLS 1.2 like connection (HelloClient, ClientKeyExchange) 
         but mostly limited to the use of Diffie Hellman as the name suggests. 
         """

         s = b"".join([f, b"(", flatten_parameters_to_bytestring(data), b")", b"\n"])
         self._send(s)

    def sendReceive(self, f, *data):
        """Sends any data needed to establish an initial connection and receive data from the sesrver"""
        self.send(f, *data)
        return self.receive()

    def sendReceiveMsg(self, f, *data):
        """Sends and receive data"""
        self.send(f, *data)
        return self.receiveEncryptedMsg()
