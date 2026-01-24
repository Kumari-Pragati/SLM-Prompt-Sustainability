import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_even([1, 3, 5, 4, 2]), 2)
        self.assertEqual(first_even([2, 4, 6, 8]), 2)
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_single_element_list(self):
        self.assertEqual(first_even([5]), -1)
        self.assertEqual(first_even([2]), 2)

    def test_all_even_list(self):
        self.assertEqual(first_even([2, 4, 6, 8]), 2)

    def test_all_odd_list(self):
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_negative_numbers(self):
        self.assertEqual(first_even([-1, -3, -5, -4, -2]), -2)
