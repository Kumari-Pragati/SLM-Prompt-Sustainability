import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_even_position(self):
        self.assertTrue(even_position([2, 4, 6, 8]))
        self.assertFalse(even_position([1, 3, 5, 7]))
        self.assertTrue(even_position([2, 4, 6, 8, 10]))
        self.assertFalse(even_position([1, 3, 5, 7, 9]))
        self.assertTrue(even_position([2, 4, 6, 8, 10, 12]))
        self.assertFalse(even_position([1, 3, 5, 7, 9, 11]))

    def test_even_position_empty(self):
        self.assertTrue(even_position([]))

    def test_even_position_single_element(self):
        self.assertTrue(even_position([2]))

    def test_even_position_single_element_odd(self):
        self.assertFalse(even_position([1]))
