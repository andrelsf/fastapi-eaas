#/project/app/service/crypto.py

from cgitb import text
from json import loads, dumps
from hashlib import sha256
from base64 import b64encode, b64decode

from fastapi import Request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from app.config import Settings

not_implemented = { 'code': 422, 'message': 'Not implemented' }

# ENCRYPT
def aes_encrypt(alg: str, mode: str, data: bytes, settings: Settings):
    if (alg == "AES" and mode == "GCM"):
        return aes_encrypt_gcm(data, settings)
    
    if (alg == "AES" and mode == "CBC"):
        return aes_encrypt_cbc(data, settings)
    
    return not_implemented


# DECRYPT
def aes_decrypt(alg: str, mode: str, data: dict, settings: Settings):
    if (alg == "AES" and mode == "GCM"):
        return aes_decrypt_gcm(data, settings)
    
    if (alg == "AES" and mode == "CBC"):
        return aes_decrypt_cbc(data, settings)
    
    return not_implemented


# AES Encrypt CBC
def aes_encrypt_cbc(data: bytes, settings: Settings):
    cipher = AES.new(settings.aes_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    
    hash_ciphered_text = sha256(ct_bytes).hexdigest()
    iv = b64encode(cipher.iv).decode('utf8')
    ciphered_text = b64encode(ct_bytes).decode('utf8')

    return { 
        'ciphertext': ciphered_text,
        'hash': hash_ciphered_text,
        'iv': iv
    }


# AES Decrypt CBC
def aes_decrypt_cbc(request: dict, settings: Settings):
    cipheredContent = b64decode(request.get('cipheredContent'))
    iv = b64decode(request.get('iv'))

    cipher = AES.new(settings.aes_key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipheredContent), AES.block_size)

    return loads(decrypted_data)


# AES Encrypt GCM
def aes_encrypt_gcm(data: bytes, settings: Settings):
    cipher = AES.new(settings.aes_key, AES.MODE_GCM)
    cipher.update(settings.aes_gcm_header)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return {
        'ciphertext': b64encode(ciphertext).decode('utf-8'),
        'nonce': b64encode(cipher.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


# AES Decrypt GCM
def aes_decrypt_gcm(request: dict, settings: Settings):
    ciphertext = b64decode(request.get('ciphertext'))
    nonce = b64decode(request.get('nonce'))
    tag = b64decode(request.get('tag'))

    cipher = AES.new(settings.aes_key, AES.MODE_GCM, nonce=nonce)
    cipher.update(settings.aes_gcm_header)
    open_data = cipher.decrypt_and_verify(ciphertext, tag)
    return loads(open_data)
