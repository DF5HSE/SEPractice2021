"""This module does blah blah."""
import math
import unittest


print('Hello')

A = math.pi
A /= 2


class Cls:
    """This class does Cls."""
    def __init__(self):
        self.x_v = 10

    def __len__(self):
        return 1

    def kek(self):
        """Return pass"""
        self.x_v = 1
        return 10

    def zhaba(self):
        """Return pass"""
        self.x_v = 2
        return 'zhaba'


def kek():
    """Return 0"""
    return 0


def kek2():
    """Return 1"""
    return 1


def kek3():
    """Return 1"""
    return 12421


class TestStringMethods(unittest.TestCase):
    """Return 1"""
    def test_upper(self):
        """Return 1"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Return 1"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Return 1"""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
