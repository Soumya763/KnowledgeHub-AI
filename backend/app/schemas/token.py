from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """
    Response returned after successful authentication.
    """
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """
    Decoded JWT payload.
    """
    sub: Optional[str] = None