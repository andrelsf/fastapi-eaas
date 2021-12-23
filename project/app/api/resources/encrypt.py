# project/app/api/resources/encrypt.py

from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from fastapi import APIRouter, Request, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.post("/crypto/encrypt")
async def postEncrypt(request: Request, settings: Settings = Depends(get_settings)):
    try:
        data: bytes = await request.body()
        key = settings.aes_key
        
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))

        iv = b64encode(cipher.iv).decode('utf8')
        ciphered_text = b64encode(ct_bytes).decode('utf8')

        return {'iv': iv, 'cipheredContent': ciphered_text}
    except (Exception):
        return {'error': 'Failed to encrypt data'}