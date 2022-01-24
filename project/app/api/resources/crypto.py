# project/app/api/crypto.py

import ast, json
from fastapi import APIRouter, Request, Depends, HTTPException

from app.config import get_settings, Settings
from app.service.crypto import aes_encrypt, aes_decrypt


router = APIRouter()


@router.post("/crypto/encrypt")
async def post_encrypt_aes_gcm(request: Request, settings: Settings = Depends(get_settings), response_model=dict[str, str, str]):
    try:
        data: bytes = await request.body()
        return aes_encrypt("AES", "GCM", data, settings)
    except (Exception):
        raise HTTPException(status_code=422, detail="Failed to encrypt data")


@router.post("/crypto/decrypt", status_code=200)
async def post_decrypt_aes_gcm(postDecryptRequest: Request, settings: Settings = Depends(get_settings)):
    try:
        request_body = await postDecryptRequest.json()
        return aes_decrypt("AES", "GCM", request_body, settings)
    except (ValueError, KeyError):
        raise HTTPException(status_code=422, detail="Failed to decrypt data")


@router.post("/crypto/encrypt/{alg}/{mode}", status_code=201)
async def post_encrypt(request: Request, alg: str, mode: str, settings: Settings = Depends(get_settings), response_model=dict[str, str, str]):
    try:
        data: bytes = await request.body()
        return aes_encrypt(alg.upper(), mode.upper(), data, settings)
    except (Exception):
        raise HTTPException(status_code=422, detail="Failed to encrypt data")


@router.post("/crypto/decrypt/{alg}/{mode}", status_code=200)
async def post_decrypt(postDecryptRequest: Request, alg: str, mode: str, settings: Settings = Depends(get_settings)):
    try:
        request_body = await postDecryptRequest.json()
        return aes_decrypt(alg.upper(), mode.upper(), request_body, settings)
    except (ValueError, KeyError):
        raise HTTPException(status_code=422, detail="Failed to decrypt data")