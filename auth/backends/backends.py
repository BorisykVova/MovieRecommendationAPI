from jose import jwt, JWTError
from pydantic import ValidationError
from passlib.context import CryptContext

from .. import errors
from .base import BaseBackend
from .schemas import Token, TokenData, TokenType

ALGORITHM = 'HS256'
SECRET_KEY = '062843e82369cbe2a3f15c25b24e4c7300c4f6d0c2059a2d76e5082b526f636e'


class PasslibBased(BaseBackend):

    _pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def verify(cls, password: str, hashed_password: str) -> bool:
        return cls._pwd_context.verify(password, hashed_password)

    @classmethod
    def create_password_hash(cls, password: str) -> str:
        return cls._pwd_context.hash(password)


class JwtBackend(PasslibBased):

    @classmethod
    def create_access_token(cls, data: TokenData) -> Token:
        jwt_token = jwt.encode(
            data.dict(exclude_none=True),
            key=SECRET_KEY,
            algorithm=ALGORITHM,
        )

        token = Token(
            access_token=jwt_token,
            token_type=TokenType.BEARER,
        )
        return token

    @classmethod
    def fetch_data(cls, access_token: str) -> TokenData:
        try:
            payload = jwt.decode(
                access_token,
                key=SECRET_KEY,
                algorithms=ALGORITHM,
            )
        except JWTError as err:
            raise errors.CredentialError(f'Bad token: {err}')

        try:
            return TokenData(**payload)
        except ValidationError as err:
            raise errors.CredentialError(f'Bad token: {err}')
