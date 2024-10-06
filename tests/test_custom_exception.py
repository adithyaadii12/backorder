""" Test the CustomException class. """

import unittest
import sys

from sys import exc_info


sys.path.append('C:\\Users\\adith\\Desktop\\backorder\\src')

from src.exception import CustomException


def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
    except ZeroDivisionError as e:
        raise CustomException(e, exc_info())
    else:
        return a / b


class TestCustomException(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(CustomException):
            divide(10, 0)

    def test_divide_by_nonzero(self):
        self.assertEqual(divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()