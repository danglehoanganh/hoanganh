import os
import json
from base64 import b64decode
from crypto_utils import *

receiver_private = load_key("keys/receiver_private.pem")
sender_public = load_key("keys/sender_public.pem")

# Nhận metadata, signature, session key (giả lập nhận thành công)
file_name = "assignment.txt"
timestamp = "timestamp-from-sender"
num_parts = 3
metadata = f"{file_name}|{timestamp}|{num_parts}".encode()
metadata_sig = "signature-from-sender"  
enc_session_key = "received-session-key"  

# Với test: dùng cùng session_key như sender
session_key = generate_session_key()  # Thay bằng session_key thực nhận trong thực tế

output = b""
for i in range(1, 4):
    with open(f"parts/part{i}.json") as f:
        part = json.load(f)

    iv = b64decode(part["iv"])
    cipher = b64decode(part["cipher"])
    hash_val = part["hash"]
    sig = b64decode(part["sig"])

    computed_hash = sha512_hash(iv + cipher)
    if hash_val != computed_hash:
        print(f"Hash mismatch at part {i}")
        print("NACK")
        exit()

    if not rsa_verify((iv + cipher).hex().encode(), sig, sender_public):
        print(f"Signature invalid at part {i}")
        print("NACK")
        exit()

    decrypted = des_decrypt(cipher, session_key, iv)
    output += decrypted

with open("assignment_received.txt", "wb") as f:
    f.write(output)

print("All parts valid. File reassembled.")
print("ACK")
