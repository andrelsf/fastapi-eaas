# project/app/api/resources/encrypt.py

import hashlib as hash
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from fastapi import APIRouter, Request, Depends, HTTPException

from app.config import get_settings, Settings


router = APIRouter()


@router.post("/crypto/encrypt", status_code=201)
async def postEncrypt(request: Request, settings: Settings = Depends(get_settings)):
    try:
        data: bytes = await request.body()
        key = settings.aes_key
        
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        
        hash_ciphered_text = hash.sha256(ct_bytes).hexdigest()

        iv = b64encode(cipher.iv).decode('utf8')
        ciphered_text = b64encode(ct_bytes).decode('utf8')

        return { 
            'cipheredContent': ciphered_text,
            'hashContent': hash_ciphered_text,
            'iv': iv
        }
    except (Exception):
        raise HTTPException(status_code=422, detail="Failed to encrypt data")