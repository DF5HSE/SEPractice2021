import unittest
from src.utils import validate_new_password
from pydantic import SecretStr


class TestPasswordValidation(unittest.TestCase):
    def test_upper(self):
        self.assertFalse(validate_new_password(SecretStr(""))[0])


if __name__ == '__main__':
    unittest.main()
    print('End')
