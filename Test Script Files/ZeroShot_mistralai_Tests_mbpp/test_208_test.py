import unittest
from mbpp_208_code import compile

def is_decimal(num):
  num_fetch = compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
  result = num_fetch.search(num)
  return bool(result)

class TestIsDecimal(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_decimal(""))

    def test_non_decimal_string(self):
        self.assertFalse(is_decimal("abc123"))
        self.assertFalse(is_decimal("123abc"))
        self.assertFalse(is_decimal("123_456"))
        self.assertFalse(is_decimal("123-456"))
        self.assertFalse(is_decimal("123e456"))
        self.assertFalse(is_decimal("123E456"))
        self.assertFalse(is_decimal("123F456"))

    def test_decimal_string_with_one_digit_after_decimal(self):
        self.assertTrue(is_decimal("1"))
        self.assertTrue(is_decimal("1.1"))
        self.assertTrue(is_decimal("1.0"))
        self.assertTrue(is_decimal("0.1"))
        self.assertTrue(is_decimal("0.0"))

    def test_decimal_string_with_two_digits_after_decimal(self):
        self.assertTrue(is_decimal("123.45"))
        self.assertTrue(is_decimal("123.00"))
        self.assertTrue(is_decimal("0.12"))
        self.assertTrue(is_decimal("0.00"))
