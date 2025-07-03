from Crypto.PublicKey import RSA
import os

def generate_rsa_keys(private_key_path, public_key_path, bits=1024):
    key = RSA.generate(bits)
    
    # Lưu private key
    with open(private_key_path, "wb") as f:
        f.write(key.export_key())
    
    # Lưu public key
    with open(public_key_path, "wb") as f:
        f.write(key.publickey().export_key())

# Tạo thư mục chứa khóa nếu chưa có
os.makedirs("keys", exist_ok=True)

# Tạo khóa cho sender
generate_rsa_keys("keys/sender_private.pem", "keys/sender_public.pem")

# Tạo khóa cho receiver
generate_rsa_keys("keys/receiver_private.pem", "keys/receiver_public.pem")

print("RSA keys generated and saved to 'keys/' folder.")
