"""users database"""
import datetime
import re

from datetime import date
from typing import Dict, Tuple, Optional


class UserMeta:  # pylint: disable=too-few-public-methods
    """User metadata"""
    num_of_users: int = 0

    def __init__(self, email: str, name: str, birth_date: date):
        self.email: str = email
        UserMeta.num_of_users += 1
        self.identifier: int = UserMeta.num_of_users
        self.name: str = name
        self.birth_date: date = birth_date


# id_pwd: Dict[int, str] = {}
# id_user_meta: Dict[int, UserMeta] = {}
# email_id: Dict[str, int] = {}
# currentUserId: Optional[int] = None


class UsersDataBase:
    """User database class"""

    def __init__(self):
        self.id_pwd: Dict[int, str] = {}
        self.id_user_meta: Dict[int, UserMeta] = {}
        self.email_id: Dict[str, int] = {}
        self.currentUserId: Optional[int] = None

    def add_user(self, email: str, password: str,
                 name: str, birth_date: date) -> Tuple[bool, str]:
        """
        :param email:
        :param password:
        :param name:
        :param birth_date:
        :return:
        """
        if re.fullmatch(r".+@.+\..+", email) is None or email.count("@") != 1:
            return False, "Invalid email"
        if email in self.email_id:
            return False, "Email already exists"
        if birth_date.year >= datetime.datetime.now().year:
            return False, "Birth year is incorrect"
        if len(name) == 0:
            return False, "Empty name"
        if len(password) == 0:
            return False, "Empty password"

        new_user_meta = UserMeta(email, name, birth_date)
        self.email_id[email] = new_user_meta.identifier
        self.id_pwd[new_user_meta.identifier] = password
        self.id_user_meta[new_user_meta.identifier] = new_user_meta
        return True, "User added"

    def authorization(self, email: str, password: str) -> Tuple[bool, str]:
        """
        :param email:
        :param password:
        :return:
        """
        if email not in self.email_id:
            return False, "Incorrect email or password"
        if self.id_pwd[self.email_id[email]] != password:
            return False, "Incorrect email or password"
        return True, "Ok"

    def get_meta_by_mail(self, email: str) -> Optional[UserMeta]:
        """
        :param email:
        :return:
        """
        if email not in self.email_id:
            return None
        identifier = self.email_id[email]
        return self.id_user_meta[identifier]

