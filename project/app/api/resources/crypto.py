# project/app/api/crypto.py

from fastapi import APIRouter, Request, Depends, HTTPException

from app.config import get_settings, Settings
from app.api.http.requests import PostDecryptRequest
from app.service.crypto import aes_encrypt_cbc, aes_decrypt_cbc


router = APIRouter()


@router.post("/crypto/encrypt", status_code=201)
async def post_encrypt(request: Request, settings: Settings = Depends(get_settings), response_model=dict[str, str, str]):
    try:
        data: bytes = await request.body()
        return aes_encrypt_cbc(data, settings)
    except (Exception):
        raise HTTPException(status_code=422, detail="Failed to encrypt data")


@router.post("/crypto/decrypt", status_code=200)
def post_decrypt(postDecryptRequest: PostDecryptRequest, settings: Settings = Depends(get_settings)):
    try:
        return aes_decrypt_cbc(postDecryptRequest, settings)
    except (ValueError, KeyError):
        raise HTTPException(status_code=422, detail="Failed to decrypt data")