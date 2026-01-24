import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_single_even_number(self):
        self.assertEqual(filter_evennumbers([4]), [4])

    def test_single_odd_number(self):
        self.assertEqual(filter_evennumbers([3]), [])

    def test_multiple_even_numbers(self):
        self.assertEqual(filter_evennumbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_multiple_odd_numbers(self):
        self.assertEqual(filter_evennumbers([1, 3, 5, 7]), [])

    def test_mixed_numbers(self):
        self.assertEqual(filter_evennumbers([2, 4, 1, 3, 5, 6]), [2, 4, 6])
