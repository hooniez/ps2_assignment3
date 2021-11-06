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
        p = parameters.parameter_numbers().p # the prime modulus value
        g = parameters.parameter_numbers().g # the generator value (must be 2 or greater)
        data = (p, g)
        b = int(self.sendReceiveDH(b"client_hello", data)) # Server public value

        a_private_key = parameters.generate_private_key() # Client secret number
        a = a_private_key.private_numbers().x
        shared_key = pow(b, a, p)

        g_pow_a_mod_p = a_private_key.public_key().public_numbers().y

        self.sendDH(b"client_key_exchange", g_pow_a_mod_p)

        print("Shared_key is " + str(shared_key))

        # Reduce the length of the shared key from DH using SHA-256
        digest = hashes.Hash(hashes.SHA256())
        digest.update(str(shared_key).encode())
        symmetric_key = digest.finalize()

        # print("Shared_key_bytes are" + str(symmetric_key))

        print(base64.urlsafe_b64encode(symmetric_key))

        self.shared_key = base64.urlsafe_b64encode(symmetric_key)


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

    def send(self, f, *data):
        """
        Sends data. Note that a trailing newline '\n' is added here

        The protocol uses CP437 encoding - https://en.wikipedia.org/wiki/Code_page_437
        which is mildly distressing as it can't encode all of Unicode.
        """
        # Use the shared key from DH hasehd with SHA-256 to encrypt a message

        

        s = b"".join([f, b"(", flatten_parameters_to_bytestring(data), b")", b"\n"])

        f = Fernet(self.shared_key)
        token = f.encrypt(s)

        self._send(token)

    def sendDH(self, f, *data):
         """
         Sends data. Note that a trailing newline '\n' is added here
 
         The protocol uses CP437 encoding - https://en.wikipedia.org/wiki/Code_page_437
         which is mildly distressing as it can't encode all of Unicode.
         """

         s = b"".join([f, b"(", flatten_parameters_to_bytestring(data), b")", b"\n"])
         self._send(s)

        

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

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()

    def sendReceiveDH(self, f, *data):
        """Sends and receive data"""
        self.sendDH(f, *data)
        return self.receive()
