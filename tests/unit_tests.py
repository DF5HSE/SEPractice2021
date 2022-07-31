import datetime
import re

import unittest
import string
import random
from src.database.users import UsersDataBase
from src.utils import validate_new_password
from pydantic import SecretStr
from datetime import date
from parameterized import parameterized

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

    def test_correct_password(self):
        n_pwds = 1000
        for _ in range(n_pwds):
            pwd = self.generate_pref()
            pwd += ''.join(random.choices(letters + digits + specials, k=random.randint(4, 12)))
            self.assertTrue(validate_new_password(SecretStr(pwd))[0])


class TestUserAdding(unittest.TestCase):
    def setUp(self):
        self.udb = UsersDataBase()

    def test_mail_correctness(self):
        self.assertFalse(self.udb.add_user("bad email", "qwerty", "John", date(2021, 1, 1))[0])

    def test_original_email(self):
        self.assertTrue(self.udb.add_user("good@kek.com", "qwerty", "John", date(2000, 1, 1))[0])
        self.assertFalse(self.udb.add_user("good@kek.com", "qwerty", "John", date(2001, 1, 1))[0])

    def test_valid_ages(self):
        prev_year = datetime.datetime.now().year - 1
        self.assertTrue(self.udb.add_user(f"best{prev_year}@kek.com", "qwerty", "John", date(prev_year, 1, 1))[0])

    def test_invalid_ages(self):
        cur_year = datetime.datetime.now().year
        self.assertFalse(self.udb.add_user(f"best{cur_year}@kek.com", "qwerty", "John", date(cur_year, 1, 1))[0])

    def test_empty_name(self):
        self.assertFalse(self.udb.add_user("best@kek.com", "qwerty", "", date(1, 1, 1))[0])

    def test_empty_password(self):
        self.assertFalse(self.udb.add_user("best@kek.com", "", "John", date(1, 1, 1))[0])

    def test_correct(self):
        for k in range(1, datetime.datetime.now().year):
            self.assertTrue(self.udb.add_user(f"best{k}@kek.com", f"qwerty{k}", "John", date(k, 1, 1))[0])
            self.assertFalse(self.udb.add_user(f"best1@kek.com", "qwerty", "John", date(k, 1, 1))[0])

    @parameterized.expand([
        ["very@bad@email.com"],
        ["ve@@ry@ba@d@em@@@@a@il@eg.co@@m"],
        ["ve@@ry@ba@d@em@@@@a@il@aasd.co@@m"],
        ["ve@@@gs.com"],
        ["ve@@@asad@f.com"],
        ["2@@@@@@@@@@@@@@@@@@@@@@@@@@s.co@@m"],
        ["2@@@@@kekekgdwqEWFsaf@@@@@@@@@@@@@@@@@@@@@s.com"],
        ["2@@@@@fgasek@@@@@@@@@@@@@@@@@@@s.com"],
        ["2@@@@@kekekekgEGAsaW@@@@@@@@@@@@@@@@@@@@@s.com"]
    ])
    def test_check_at_in_mail(self, mail):
        self.assertFalse(self.udb.add_user(mail, "qwerty", "John", date(2001, 1, 1))[0])


class TestUserAuth(unittest.TestCase):
    def setUp(self):
        self.udb = UsersDataBase()

    def test_invalid_mail(self):
        self.assertFalse(self.udb.authorization("best@kek.com", "pwd")[0])

    def test_invalid_password(self):
        self.udb.add_user("best@kek.com", "qwerty", "gqogdGASsdafhn", date(2001, 1, 1))
        self.assertFalse(self.udb.authorization("best@kek.com", "pwd")[0])

    def test_correct(self):
        self.udb.add_user("best@kek.com", "qwerty", "gqogdGASsdafhn", date(2001, 1, 1))
        self.assertFalse(self.udb.authorization("best@kek.com", "pwd")[0])
        self.assertFalse(self.udb.authorization("best1337@kek.com", "qwerty")[0])
        self.assertTrue(self.udb.authorization("best@kek.com", "qwerty")[0])
        self.assertFalse(self.udb.authorization("best2@kek.com", "qwerty")[0])
        self.udb.add_user("best2@kek.com", "qwerty2", "gqogdGASsdafhn", date(2001, 1, 1))
        self.assertFalse(self.udb.authorization("best@kek.com", "qwerty2")[0])
        self.assertFalse(self.udb.authorization("best2@kek.com", "qwerty")[0])
        self.assertTrue(self.udb.authorization("best2@kek.com", "qwerty2")[0])
        self.udb.add_user("bestkek.com", "qwerty", "gqogdGASsdafhn", date(2001, 1, 1))
        self.assertFalse(self.udb.authorization("bestkek.com", "qwerty")[0])


class TestGetUserMeta(unittest.TestCase):
    def setUp(self):
        self.udb = UsersDataBase()

    def test_invalid_mail(self):
        self.assertIsNone(self.udb.get_meta_by_mail("best@kek.com"))

    def test_correct_user_data(self):
        email = "best@kek.com"
        password = "qwerty"
        name = "gqogdGASsdafhn"
        birth_date = date(2001, 1, 1)
        self.udb.add_user(email, password, name, birth_date)
        self.assertIsNotNone(self.udb.get_meta_by_mail(email))
        meta = self.udb.get_meta_by_mail(email)
        self.assertEquals(email, meta.email)
        self.assertEquals(name, meta.name)
        self.assertEquals(birth_date, meta.birth_date)


if __name__ == '__main__':
    unittest.main()
    print('End')
