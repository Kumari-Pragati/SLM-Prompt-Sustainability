import unittest
from179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_num_keith(12345))
        self.assertTrue(is_num_keith(98765))
        self.assertTrue(is_num_keith(123))
        self.assertTrue(is_num_keith(987))

    def test_zero(self):
        self.assertTrue(is_num_keith(0))

    def test_negative_numbers(self):
        self.assertFalse(is_num_keith(-12345))
        self.assertFalse(is_num_keith(-98765))
        self.assertFalse(is_num_keith(-123))
        self.assertFalse(is_num_keith(-987))

    def test_long_numbers(self):
        self.assertTrue(is_num_keith(1234567890))

    def test_single_digit_numbers(self):
        for num in range(10):
            self.assertTrue(is_num_keith(num))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0 * 10 ** 10))
        self.assertFalse(is_num_keith((10 ** 10) + 1))
        self.assertFalse(is_num_keith((10 ** 10) - 1))
