import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_keith_number(self):
        self.assertTrue(is_num_keith(123456789))

    def test_non_keith_number(self):
        self.assertFalse(is_num_keith(12345678))

    def test_edge_case_zero(self):
        self.assertTrue(is_num_keith(0))

    def test_edge_case_one(self):
        self.assertTrue(is_num_keith(1))

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            is_num_keith(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            is_num_keith('123')

    def test_edge_case_large_number(self):
        self.assertTrue(is_num_keith(1234567890123456789))
