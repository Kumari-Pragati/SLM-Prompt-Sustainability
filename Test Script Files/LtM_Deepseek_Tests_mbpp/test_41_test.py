import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4]), [2, 4])

    def test_empty_input(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_all_even_input(self):
        self.assertEqual(filter_evennumbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_all_odd_input(self):
        self.assertEqual(filter_evennumbers([1, 3, 5, 7]), [])

    def test_mixed_input(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_negative_numbers(self):
        self.assertEqual(filter_evennumbers([-1, -2, -3, -4]), [-2, -4])

    def test_large_numbers(self):
        self.assertEqual(filter_evennumbers(list(range(1, 101))), list(range(2, 101, 2)))
