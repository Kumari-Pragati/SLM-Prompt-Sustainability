import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(filter_evennumbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_all_odd_numbers(self):
        self.assertEqual(filter_evennumbers([1, 3, 5, 7]), [])

    def test_single_even_number(self):
        self.assertEqual(filter_evennumbers([1]), [])

    def test_single_odd_number(self):
        self.assertEqual(filter_evennumbers([2]), [2])

    def test_negative_numbers(self):
        self.assertEqual(filter_evennumbers([-1, -2, -3, -4]), [-2, -4])

    def test_zero(self):
        self.assertEqual(filter_evennumbers([0]), [0])
