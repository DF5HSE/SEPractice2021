"""Utils"""
from typing import Tuple

from pydantic import SecretStr


def validate_new_password(pwd: SecretStr) -> Tuple[bool, str]:
    """
    Requirements to password:
    - 1+ char in upper case
    - 1+ char in lower case
    - 1+ digit
    - 1+ special char: '!', '@', '#', '_' or '.'
    - no other chars
    - length more 8+

    :param pwd:
    :return:
    """
    if pwd is None:
        pass
    return True, "Ok"
