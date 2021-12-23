# project/app/api/resources/decrypt.py

import json
from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from fastapi import APIRouter, Depends, HTTPException

from app.config import get_settings, Settings
from app.api.http.requests import PostDecryptRequest


router = APIRouter()


@router.post("/crypto/decrypt", status_code=200)
def postDecrypt(postDecryptRequest: PostDecryptRequest, settings: Settings = Depends(get_settings)):
    try:
        key = settings.aes_key
        
        cipheredContent = b64decode(postDecryptRequest.cipheredContent)
        iv = b64decode(postDecryptRequest.iv)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decryptedData = unpad(cipher.decrypt(cipheredContent), AES.block_size)

        return json.loads(decryptedData)
    except (ValueError, KeyError):
        raise HTTPException(status_code=422, detail="Failed to decrypt data")