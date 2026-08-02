from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_access_token

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(auth: AuthInput):
    # For demonstration purposes, hardcoded credentials are used.
    # In a real application, the username and password would be validated against a database.
    if auth.username == 'admin' and auth.password == 'password':
        token = create_access_token({"sub": auth.username})
        return {"access_token": token, "token_type": "bearer"}
    else:
        return {"error": "Invalid username or password"}