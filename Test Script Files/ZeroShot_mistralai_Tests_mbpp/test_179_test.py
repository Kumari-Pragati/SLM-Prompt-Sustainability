import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_is_num_keith_positive_numbers(self):
        self.assertTrue(is_num_keith(12345))
        self.assertTrue(is_num_keith(54321))
        self.assertTrue(is_num_keith(98765))
        self.assertTrue(is_num_keith(123))
        self.assertTrue(is_num_keith(456))
        self.assertTrue(is_num_keith(789))

    def test_is_num_keith_zero(self):
        self.assertTrue(is_num_keith(0))

    def test_is_num_keith_negative_numbers(self):
        self.assertFalse(is_num_keith(-12345))
        self.assertFalse(is_num_keith(-54321))
        self.assertFalse(is_num_keith(-98765))

    def test_is_num_keith_non_integer_numbers(self):
        self.assertFalse(is_num_keith(3.14))
        self.assertFalse(is_num_keith(-2.718))
