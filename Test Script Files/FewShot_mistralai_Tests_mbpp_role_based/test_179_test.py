import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_keith_number(self):
        self.assertTrue(is_num_keith(179))

    def test_non_keith_number_less_than_10(self):
        self.assertFalse(is_num_keith(9))

    def test_non_keith_number_greater_than_10_and_less_than_100(self):
        self.assertFalse(is_num_keith(99))

    def test_non_keith_number_greater_than_100(self):
        self.assertFalse(is_num_keith(1000))

    def test_negative_number(self):
        self.assertFalse(is_num_keith(-1))

    def test_zero(self):
        self.assertFalse(is_num_keith(0))

    def test_floating_point_number(self):
        self.assertFalse(is_num_keith(179.5))
