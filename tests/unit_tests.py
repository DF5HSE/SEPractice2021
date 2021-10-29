import re

import unittest
import string
import random
import src.database.user as udb
from src.database.user import id_user_meta, email_id, id_pwd
from src.utils import validate_new_password
from pydantic import SecretStr
from datetime import date

digits = '0123456789'
letters = string.ascii_letters
specials = '!@#_.'


class TestPasswordValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        random.seed(42)

    def test_empty(self):
        self.assertFalse(validate_new_password(SecretStr(""))[0])

    def test_chars_correctness(self):
        n_pwds = 1000
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
                pwd += ''.join(random.choices(symbs, k=random.randint(5, 13)))
                self.assertFalse(validate_new_password(SecretStr(pwd))[0])

    def generate_pref(self):
        return random.choice(letters.lower()) + random.choice(digits) + random.choice(specials) + random.choice(
            letters.upper())

    def test_len(self):
        n_pwds = 1000
        symbs = letters + digits + specials

        for _ in range(n_pwds):
            pwd = self.generate_pref()
            pwd += ''.join(random.choices(symbs, k=random.randint(0, 3)))
            self.assertFalse(validate_new_password(SecretStr(pwd))[0])
            pwd = self.generate_pref()
            pwd += ''.join(random.choices(symbs, k=random.randint(13, 100)))
            self.assertFalse(validate_new_password(SecretStr(pwd))[0])

    def test_forbidden(self):
        n_pwds = 1000
        for _ in range(n_pwds):
            pwd = self.generate_pref()
            pwd += ''.join(map(chr, [random.randint(0, 255) for _ in range(random.randint(4, 12))]))
            while re.search(r'[^0-9a-zA-Z!@#_.]', pwd) is None:
                pwd = self.generate_pref()
                pwd += ''.join(map(chr, [random.randint(0, 255) for _ in range(random.randint(4, 12))]))
            pwd = ''.join(random.sample(pwd, len(pwd)))
            self.assertFalse(validate_new_password(SecretStr(pwd))[0])


class TestUserAdding(unittest.TestCase):
    def setUp(self):
        id_user_meta.clear()
        id_pwd.clear()
        email_id.clear()

    def test_mail_correctness(self):
        self.assertFalse(udb.add_user("bad email", "qwerty", "John", date(2021, 1, 1)))


if __name__ == '__main__':
    unittest.main()
    print('End')
