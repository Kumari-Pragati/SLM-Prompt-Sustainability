import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_true_case(self):
        self.assertTrue(is_num_keith(123))

    def test_false_case(self):
        self.assertFalse(is_num_keith(456))

    def test_edge_case_zero(self):
        self.assertFalse(is_num_keith(0))

    def test_edge_case_one(self):
        self.assertTrue(is_num_keith(1))

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            is_num_keith(-123)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            is_num_keith('abc')
