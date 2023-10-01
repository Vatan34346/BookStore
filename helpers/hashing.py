from passlib.context import CryptContext


class Hash:
    """develpoer: panteleimon gvichia"""
    """crypting an decrypting password"""
    def __init__(self):
        self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def bcrypt(self, password):
        return self.pwd_context.hash(password)

    def verify(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
