import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_typical_odd(self):
        self.assertTrue(is_odd(3))

    def test_typical_even(self):
        self.assertFalse(is_odd(4))

    def test_edge_case_zero(self):
        self.assertFalse(is_odd(0))

    def test_edge_case_negative(self):
        self.assertFalse(is_odd(-3))

    def test_edge_case_one(self):
        self.assertTrue(is_odd(1))

    def test_edge_case_large_odd(self):
        self.assertTrue(is_odd(999))

    def test_edge_case_large_even(self):
        self.assertFalse(is_odd(1000))

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            is_odd('abc')

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            is_odd([1, 2, 3])
