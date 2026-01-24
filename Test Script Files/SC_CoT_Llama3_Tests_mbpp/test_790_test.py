import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_even_position_typical(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_even_position_edge(self):
        self.assertTrue(even_position([0, 0, 2, 2, 4, 4]))

    def test_even_position_all_even(self):
        self.assertTrue(even_position([0, 0, 0, 0, 0, 0]))

    def test_even_position_all_odd(self):
        self.assertFalse(even_position([1, 1, 1, 1, 1, 1]))

    def test_even_position_mixed(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_even_position_empty(self):
        self.assertTrue(even_position([]))

    def test_even_position_single_element(self):
        self.assertTrue(even_position([0]))

    def test_even_position_single_odd(self):
        self.assertFalse(even_position([1]))

    def test_even_position_invalid_input(self):
        with self.assertRaises(TypeError):
            even_position('invalid input')
