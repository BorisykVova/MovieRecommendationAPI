from abc import ABC, abstractmethod


class BaseBackend(ABC):

    # _pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    @abstractmethod
    def verify(cls, password: str, hashed_password: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def create_password_hash(cls, password: str) -> str:
        pass

