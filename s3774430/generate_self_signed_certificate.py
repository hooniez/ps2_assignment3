from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
import datetime

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

with open("key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"password")

    ))

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"AU"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Victoria"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, U"Melbourne"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Minecraft Server"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"192.168.56.1"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be vaild for 30 days
    datetime.datetime.utcnow() + datetime.timedelta(days=30)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False
).sign(key, hashes.SHA256())

with open("certificate.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
