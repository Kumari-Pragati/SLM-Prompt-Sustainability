import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element(self):
        self.assertTrue(even_position([1]))
        self.assertFalse(even_position([0]))

    def test_even_length_list(self):
        self.assertTrue(even_position([0, 2, 4, 6]))
        self.assertFalse(even_position([1, 3, 5, 7]))

    def test_odd_length_list(self):
        self.assertFalse(even_position([0, 2, 4, 6, 8]))
        self.assertTrue(even_position([1, 3, 5, 7, 9]))
