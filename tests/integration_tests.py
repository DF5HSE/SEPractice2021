from unittest import TestCase
from fastapi.testclient import TestClient
from src.database.users import id_user_meta, email_id, id_pwd
from main import app

client = TestClient(app)


class TestRegistration(TestCase):
    def setUp(self):
        id_user_meta.clear()
        id_pwd.clear()
        email_id.clear()

    def test_registration_success(self):
        rs = client.post("/users/registration",
                         json={
                             "email": "a@yandex.ru",
                             "name": "a",
                             "password": "Aaaaaa1!",
                             "birth_date": "2020-01-01"
                         })
        self.assertTrue(rs.ok, rs.text)

    def test_registration_wrong_pwd_format(self):
        rs = client.post("/users/registration",
                         json={
                             "email": "a@yandex.ru",
                             "name": "a",
                             "password": "Aaaaaa!",
                             "birth_date": "2020-01-01"
                         })
        self.assertFalse(rs.ok)

    def test_registration_mail_occupied(self):
        rs = client.post("/users/registration",
                         json={
                             "email": "a@yandex.ru",
                             "name": "a",
                             "password": "Aaaaaa1!",
                             "birth_date": "2020-01-01"
                         })
        self.assertTrue(rs.ok, rs.text)
        rs = client.post("/users/registration",
                         json={
                             "email": "a@yandex.ru",
                             "name": "a",
                             "password": "Aaaaaa1!",
                             "birth_date": "2020-01-01"
                         })
        self.assertFalse(rs.ok)


class TestAuth(TestCase):
    def setUp(self):
        id_user_meta.clear()
        id_pwd.clear()
        email_id.clear()
        rs = client.post("/users/registration",
                         json={
                             "email": "a@yandex.ru",
                             "name": "ab",
                             "password": "Aaaaaa1!",
                             "birth_date": "2020-01-01"
                         })
        self.assertTrue(rs.ok, rs.text)

    def test_auth_success(self):
        rs = client.post("/users/auth", json={"email": "a@yandex.ru", "password": "Aaaaaa1!"})
        self.assertTrue(rs.ok, rs.text)

    def test_auth_user_not_exist(self):
        rs = client.post("/users/auth", json={"email": "b@yandex.ru", "password": "Aa1!"})
        self.assertFalse(rs.ok)

    def test_auth_wrong_password(self):
        rs = client.post("/users/auth", json={"email": "a@yandex.ru", "password": "Ba1!"})
        self.assertFalse(rs.ok)
