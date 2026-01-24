import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_nonagonal_numbers(self):
        self.assertTrue(is_nonagonal(1))
        self.assertTrue(is_nonagonal(7))
        self.assertTrue(is_nonagonal(14))
        self.assertTrue(is_nonagonal(22))
        self.assertTrue(is_nonagonal(30))

    def test_nonagonal_numbers_edge_cases(self):
        self.assertFalse(is_nonagonal(0))
        self.assertFalse(is_nonagonal(-1))

    def test_nonagonal_numbers_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
        with self.assertRaises(TypeError):
            is_nonagonal(None)
        with self.assertRaises(TypeError):
            is_nonagonal(1.5)

    def test_nonagonal_numbers_random_inputs(self):
        self.assertFalse(is_nonagonal(2))
        self.assertFalse(is_nonagonal(3))
        self.assertFalse(is_nonagonal(4))
        self.assertFalse(is_nonagonal(5))
        self.assertFalse(is_nonagonal(6))
