import unittest
from helpers import hash_
from .test_factory import password, password_2


class TestSQLService(unittest.TestCase):
    """
    dev: panteleimon gvichia
    description: this class test Hashing class that works with db.
    phone: +7995123456
    """

    def setUp(self):
        self.hashing = hash_

    def test_bcrypt(self):
        hashed_password = self.hashing.bcrypt(password)
        hashed_password2 = self.hashing.bcrypt(password_2)

        # happy path
        self.assertTrue(self.hashing.verify(password, hashed_password))
        self.assertTrue(self.hashing.verify(password_2, hashed_password2))

        # unhappy path
        self.assertFalse(self.hashing.verify(password_2, hashed_password))
        self.assertFalse(self.hashing.verify(password, hashed_password2))

    def test_verify(self):
        hashed_password = self.hashing.bcrypt(password)

        # happy path (valid password)
        self.assertTrue(self.hashing.verify(password, hashed_password))

        # unhappy path (invalid password)
        self.assertFalse(self.hashing.verify(password_2, hashed_password))


if __name__ == '__main__':
    unittest.main()
