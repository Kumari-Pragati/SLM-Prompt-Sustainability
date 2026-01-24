import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_even_position_typical(self):
        self.assertTrue(even_position([2, 4, 6, 8, 10]))

    def test_even_position_odd(self):
        self.assertFalse(even_position([1, 3, 5, 7, 9]))

    def test_even_position_mixed(self):
        self.assertTrue(even_position([2, 1, 4, 3, 6, 5, 8, 7, 10]))

    def test_even_position_empty(self):
        self.assertTrue(even_position([]))

    def test_even_position_single(self):
        self.assertTrue(even_position([2]))

    def test_even_position_single_odd(self):
        self.assertFalse(even_position([1]))

    def test_even_position_invalid_input(self):
        with self.assertRaises(TypeError):
            even_position('abc')
