import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_even_position_true(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_even_position_false(self):
        self.assertFalse(even_position([0, 1, 2, 3, 4, 6]))

    def test_even_position_empty(self):
        self.assertTrue(even_position([]))

    def test_even_position_single_element(self):
        self.assertTrue(even_position([0]))

    def test_even_position_negative_numbers(self):
        self.assertTrue(even_position([-2, -1, 0, 1, 2]))

    def test_even_position_mixed_numbers(self):
        self.assertFalse(even_position([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
