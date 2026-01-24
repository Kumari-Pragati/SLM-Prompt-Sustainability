import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_odd_numbers_list(self):
        self.assertEqual(first_even([1, 3, 5, 7, 9]), -1)

    def test_even_numbers_list(self):
        self.assertEqual(first_even([0, 2, 4, 6, 8]), 0)

    def test_single_number_list(self):
        self.assertEqual(first_even([1]), -1)
        self.assertEqual(first_even([2]), 2)

    def test_mixed_numbers_list(self):
        self.assertEqual(first_even([0, 1, 2, 3, 4, 5, 6, 7, 8]), 0)
