from datetime import datetime, timedelta

from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from config import JWT_SECRET_KEY, JWT_REFRESH_SECRET_KEY


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 60 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """Returns hashed password."""
    return password_context.hash(password)


def create_access_token_by_(user_email: str) -> str:
    """Creates access token for given user."""
    expires_delta = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"exp": expires_delta, "sub": str(user_email)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token_by_(user_email: str) -> str:
    """Creates refresh token for given user."""
    expires_delta = datetime.utcnow() + timedelta(
        minutes=REFRESH_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"exp": expires_delta, "sub": str(user_email)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_(token: str) -> dict:
    """Verifies an access token and returns the 'sub' claim if valid."""
    error = email = None
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        email = decoded_token.get("sub")
        if email is None:
            raise JWTError
    except ExpiredSignatureError:
        error = "Token has expired"
    except JWTError:
        error = "Invalid token"
    finally:
        return {"error": error, "email": email}
