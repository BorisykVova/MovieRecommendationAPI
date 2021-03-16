class AuthError(Exception):
    pass


class CredentialError(AuthError):
    pass


class PasswordVerifyError(CredentialError):
    pass


class EmailVerifyError(CredentialError):
    pass

