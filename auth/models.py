from tortoise import fields, models
from tortoise.exceptions import DoesNotExist

from .backends import JwtBackend, Token, TokenData
from .errors import EmailVerifyError, PasswordVerifyError


class User(models.Model):
    is_admin = fields.BooleanField(default=False)
    hashed_password = fields.CharField(max_length=512)
    email = fields.CharField(max_length=100, unique=True)
    username = fields.CharField(max_length=100, unique=True)

    def __init__(self, username: str, email: str, password: str, is_admin: bool = False):
        super().__init__(
            username=username,
            email=email,
            is_admin=is_admin,
        )
        self._set_password(password)

    @property
    def password(self) -> str:
        return self.hashed_password

    @password.setter
    def password(self, plain_password: str):
        self._set_password(plain_password)

    def verify_password(self, password: str) -> bool:
        return JwtBackend.verify(password, self.hashed_password)

    def create_token(self) -> Token:
        data = TokenData(username=self.username)
        return JwtBackend.create_access_token(data)

    def _set_password(self, plain_password: str):
        self.hashed_password = JwtBackend.create_password_hash(plain_password)

    @classmethod
    async def get_current_user(cls, access_token: str) -> 'User':
        token_data = JwtBackend.fetch_data(access_token)

        try:
            user = await User.get(username=token_data.username)
        except DoesNotExist:
            raise EmailVerifyError(f'Username {token_data.username!r} is not exists')

        return user

    @classmethod
    async def authenticate(cls, username: str, password: str) -> 'User':

        try:
            user = await User.get(username=username)
        except DoesNotExist:
            raise EmailVerifyError(f'User with username {username!r} does no exist')

        if not user.verify_password(password):
            raise PasswordVerifyError('Wrong password')

        return user
