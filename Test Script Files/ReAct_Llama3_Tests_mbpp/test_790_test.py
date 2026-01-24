import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element_list(self):
        self.assertTrue(even_position([1]))

    def test_all_even_position(self):
        self.assertTrue(even_position([0, 2, 4, 6]))

    def test_all_odd_position(self):
        self.assertTrue(even_position([1, 3, 5, 7]))

    def test_mixed_position(self):
        self.assertTrue(even_position([0, 1, 2, 3]))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            even_position(['a', 'b', 'c'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            even_position(123)
