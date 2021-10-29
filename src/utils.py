"""Utils"""
from typing import Tuple

from pydantic import SecretStr
import re


def validate_new_password(pwd: SecretStr) -> Tuple[bool, str]:
    """
    Requirements to password:

    - 1+ char in upper case
    - 1+ char in lower case
    - 1+ digit
    - 1+ special char: '!', '@', '#', '_' or '.'
    - no other chars

    - length more 8
    - length less 16

    :param pwd:
    :return:
    """
    if pwd.get_secret_value() == "":
        return False, "Password is empty"

    regs = [r'[A-Z]', r'[a-z]', r'[0-9]', r'[!@#_.]']
    reasons = ['uppercase letter', 
        'lowercase letter',
        'digit',
        'special symbol']

    for reg_exp, reason in zip(regs, reasons):
        if re.search(reg_exp, pwd.get_secret_value()) is None:
            return False, f"No {reason}"

    if not 8 <= len(pwd.get_secret_value()) <= 16:
        return False, "Wrong length of password"

    return True, "Ok"
