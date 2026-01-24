import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Odd_Occurrence([20, 10, 20, 30, 10, 10], 6), 30)

    def test_single_element(self):
        self.assertEqual(get_Odd_Occurrence([5], 1), 5)

    def test_no_odd_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([20, 20, 20], 3), -1)

    def test_negative_numbers(self):
        self.assertEqual(get_Odd_Occurrence([-20, -10, -20, -30, -10, -10], 6), -30)

    def test_large_numbers(self):
        self.assertEqual(get_Odd_Occurrence([1000000, 2000000, 1000000, 3000000, 2000000, 2000000], 6), 3000000)

    def test_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)
