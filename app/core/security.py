# Create and verify JWT tokens for authentication and authorization

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional
from jose import jwt, JWTError
from app.core.config import settings

# Helper functions
def create_access_token(data: Dict[str, Any], expires_minutes: int = 30) -> str:
    to_encode: Dict[str, Any] = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    # use UNIX timestamp for the exp claim so it's JSON-serializable
    to_encode.update({"exp": int(expire.timestamp())})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[Dict[str, Any]]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError:
        return None
    