import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 1))
        self.assertTrue(greater_specificnum([10, 20, 30, 40, 50], 10))
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))
        self.assertFalse(greater_specificnum([10, 20, 30, 40, 50], 60))

    def test_empty_list(self):
        self.assertTrue(greater_specificnum([], 1))
        self.assertTrue(greater_specificnum([], 0))

    def test_single_element(self):
        self.assertTrue(greater_specificnum([10], 10))
        self.assertFalse(greater_specificnum([10], 11))

    def test_negative_numbers(self):
        self.assertTrue(greater_specificnum([-1, -2, -3, -4, -5], -6))
        self.assertFalse(greater_specificnum([-1, -2, -3, -4, -5], 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            greater_specificnum("not a list", 1)
        with self.assertRaises(TypeError):
            greater_specificnum([1, 2, "not a number"], 1)
