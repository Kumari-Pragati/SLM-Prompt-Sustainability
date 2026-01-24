import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_even_length_list(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5]))

    def test_odd_length_list(self):
        self.assertTrue(odd_position([1, 2, 3, 5, 6]))

    def test_all_odd(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_all_even(self):
        self.assertTrue(odd_position([2, 4, 6, 8, 10]))

    def test_mixed(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_single_element_list(self):
        self.assertTrue(odd_position([1]))

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            odd_position([1, 2, 'a', 4, 5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            odd_position(123)
