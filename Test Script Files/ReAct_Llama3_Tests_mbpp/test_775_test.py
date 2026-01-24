import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_all_odd(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_all_even(self):
        self.assertTrue(odd_position([0, 2, 4, 6, 8]))

    def test_mixed(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_single_element(self):
        self.assertTrue(odd_position([1]))

    def test_all_odd_position(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_all_even_position(self):
        self.assertTrue(odd_position([0, 2, 4, 6, 8]))

    def test_mixed_position(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_position("not a list")
