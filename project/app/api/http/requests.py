#project/app/api/http/requests/postdecryptrequest.py


from pydantic import BaseModel


class PostDecryptRequest(BaseModel):
    cipheredContent: str
    hashContent: str
    iv: str