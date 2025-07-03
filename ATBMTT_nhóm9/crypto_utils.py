from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, DES
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64
import os
import json
from datetime import datetime

def load_key(path):
    with open(path, "rb") as f:
        return RSA.import_key(f.read())

def generate_session_key():
    return get_random_bytes(8)  # DES key 8 bytes

def rsa_encrypt(data, public_key):
    cipher = PKCS1_v1_5.new(public_key)
    return cipher.encrypt(data)

def rsa_sign(data, private_key):
    h = SHA512.new(data)
    return pkcs1_15.new(private_key).sign(h)

def rsa_verify(data, signature, public_key):
    h = SHA512.new(data)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

def des_encrypt(data, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    pad_len = 8 - len(data) % 8
    data += bytes([pad_len] * pad_len)
    return cipher.encrypt(data)

def des_decrypt(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    data = cipher.decrypt(ciphertext)
    pad_len = data[-1]
    return data[:-pad_len]

def sha512_hash(data):
    return SHA512.new(data).hexdigest()

def split_file(file_path, num_parts=3):
    with open(file_path, "rb") as f:
        data = f.read()
    part_size = len(data) // num_parts
    return [data[i*part_size : (i+1)*part_size] if i != num_parts - 1 else data[i*part_size:]
            for i in range(num_parts)]
