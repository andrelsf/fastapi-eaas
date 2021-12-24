#/project/app/service/crypto.py

from json import loads
from hashlib import sha256
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from app.config import Settings
from app.api.http.requests import PostDecryptRequest


# AES Encrypt CBC
def aes_encrypt_cbc(data: bytes, settings: Settings):
    cipher = AES.new(settings.aes_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    
    hash_ciphered_text = sha256(ct_bytes).hexdigest()
    iv = b64encode(cipher.iv).decode('utf8')
    ciphered_text = b64encode(ct_bytes).decode('utf8')

    return { 
        'cipheredContent': ciphered_text,
        'hashContent': hash_ciphered_text,
        'iv': iv
    }


# AES Decrypt CBC
def aes_decrypt_cbc(request: PostDecryptRequest, settings: Settings):
    cipheredContent = b64decode(request.cipheredContent)
    iv = b64decode(request.iv)

    cipher = AES.new(settings.aes_key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipheredContent), AES.block_size)

    return loads(decrypted_data)

