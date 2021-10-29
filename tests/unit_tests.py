import unittest
import string
import random
from src.utils import validate_new_password
from pydantic import SecretStr


digits = '0123456789'
letters = string.ascii_letters
specials = '!@#_.'


class TestPasswordValidation(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(validate_new_password(SecretStr(""))[0])

    def test_chars_correctness(self):
        n_pwds = 100
        lowers = letters[:26].lower()
        uppers = letters[:26].upper()
        list_of_required_groups_of_chars = [lowers, uppers, digits, specials]
        for i in range(len(list_of_required_groups_of_chars)):
            for _ in range(n_pwds):
                pwd = ""
                symbs = ""
                for j in range(len(list_of_required_groups_of_chars)):
                    if i != j:
                        pwd += random.choice(list_of_required_groups_of_chars[j])
                        symbs += list_of_required_groups_of_chars[j]
                pwd += ''.join(random.choices(symbs, k=random.randint(5, 14)))
                self.assertFalse(validate_new_password(SecretStr(pwd))[0])

    def test_len(self):
        n_pwds = 100
        symbs = letters + digits + specials

        for _ in range(n_pwds):
            pwd = random.choice(letters.lower()) + random.choice(digits) + random.choice(specials) + random.choice(letters.upper())
            pwd += ''.join(random.choices(symbs, k=random.randint(0, 3)))
            self.assertFalse(validate_new_password(SecretStr(pwd))[0])
            pwd += ''.join(random.choices(symbs, k=random.randint(12, 100)))
            self.assertFalse(validate_new_password(SecretStr(pwd))[0])



if __name__ == '__main__':
    unittest.main()
    print('End')
