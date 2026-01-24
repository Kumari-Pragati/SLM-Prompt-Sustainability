import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_empty(self):
        self.assertFalse(even_position([]))

    def test_single_element(self):
        self.assertTrue(even_position([0]))

    def test_all_even(self):
        self.assertTrue(even_position([0, 2, 4, 6, 8]))

    def test_all_odd(self):
        self.assertFalse(even_position([1, 3, 5, 7]))

    def test_mixed(self):
        self.assertFalse(even_position([0, 1, 2, 3, 4, 5, 6]))

    def test_long(self):
        self.assertTrue(even_position([0, 2, 4, 6, 8, 10, 12]))
