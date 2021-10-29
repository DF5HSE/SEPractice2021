"""users database"""
import datetime
import re

from datetime import date
from typing import Dict, Tuple


class UserMeta:  # pylint: disable=too-few-public-methods
    """User metadata"""
    num_of_users: int = 0

    def __init__(self, email: str, name: str, birth_date: date):
        self.email: str = email
        UserMeta.num_of_users += 1
        self.identifier: int = UserMeta.num_of_users
        self.name: str = name
        self.birth_date: date = birth_date


id_pwd: Dict[int, str] = {}
id_user_meta: Dict[int, UserMeta] = {}
email_id: Dict[str, int] = {}


def add_user(email: str, password: str,
             name: str, birth_date: date) -> Tuple[bool, str]:
    """
    :param email:
    :param password:
    :param name:
    :param birth_date:
    :return:
    """
    if re.search(r".+@.+\..+", email) is None:
        return False, "Invalid email"
    if email in email_id:
        return False, "Email already exists"
    if birth_date.year >= datetime.datetime.now().year:
        return False, "Birth year is incorrect"
    if len(name) == 0:
        return False, "Empty name"
    if len(password) == 0:
        return False, "Empty password"

    new_user_meta = UserMeta(email, name, birth_date)
    email_id[email] = new_user_meta.identifier
    id_pwd[new_user_meta.identifier] = password
    id_user_meta[new_user_meta.identifier] = new_user_meta
    return True, "User added"
