import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_odd([1, 2, 3, 4]), [2, 4])

    def test_empty_input(self):
        self.assertEqual(remove_odd([]), [])

    def test_all_odd_input(self):
        self.assertEqual(remove_odd([1, 3, 5]), [])

    def test_all_even_input(self):
        self.assertEqual(remove_odd([2, 4, 6]), [2, 4, 6])

    def test_mixed_input(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_negative_numbers(self):
        self.assertEqual(remove_odd([-1, -2, -3, -4]), [-2, -4])

    def test_large_numbers(self):
        self.assertEqual(remove_odd([1000000001, 1000000002]), [1000000002])
