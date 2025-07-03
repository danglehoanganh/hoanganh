import os
import json
from base64 import b64encode
from datetime import datetime
from crypto_utils import *

# Load keys
sender_private = load_key("keys/sender_private.pem")
receiver_public = load_key("keys/receiver_public.pem")

# Step 1: Handshake
print("Sender: Hello!")
print("Receiver: Ready!")  # Giả lập phản hồi

# Step 2: Tạo metadata và ký
file_name = "assignment.txt"
parts = split_file(file_name)
timestamp = datetime.utcnow().isoformat()
metadata = f"{file_name}|{timestamp}|{len(parts)}".encode()
metadata_sig = rsa_sign(metadata, sender_private)

# Mã hóa session key
session_key = generate_session_key()
enc_session_key = rsa_encrypt(session_key, receiver_public)

# Gửi metadata, chữ ký, và session key
print("Sending metadata, signature, and encrypted session key...")

# Step 3: Encrypt từng phần
os.makedirs("parts", exist_ok=True)
for i, part in enumerate(parts):
    iv = get_random_bytes(8)
    cipher = des_encrypt(part, session_key, iv)
    hash_val = sha512_hash(iv + cipher)
    sig = rsa_sign((iv + cipher).hex().encode(), sender_private)

    part_json = {
        "iv": b64encode(iv).decode(),
        "cipher": b64encode(cipher).decode(),
        "hash": hash_val,
        "sig": b64encode(sig).decode()
    }

    with open(f"parts/part{i+1}.json", "w") as f:
        json.dump(part_json, f, indent=2)

print("Sender: All parts sent.")
