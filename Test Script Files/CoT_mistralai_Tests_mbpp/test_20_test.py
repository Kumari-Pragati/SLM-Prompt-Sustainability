import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_even_numbers(self):
        for num in range(2, 10):
            self.assertFalse(is_woodall(num))

    def test_odd_numbers(self):
        self.assertTrue(is_woodall(1))
        for num in range(3, 21):
            self.assertTrue(is_woodall(num))

    def test_edge_cases(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(20))
        self.assertFalse(is_woodall(21))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_woodall, 'a')
        self.assertRaises(TypeError, is_woodall, 0.5)
