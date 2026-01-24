import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_even([2, 4, 1, 3, 6]), 2)
        self.assertEqual(first_even([4, 6, 8]), 4)
        self.assertEqual(first_even([0, 2, 4, 6]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_edge_case_single_number(self):
        self.assertEqual(first_even([1]), -1)
        self.assertEqual(first_even([3]), -1)

    def test_edge_case_odd_numbers(self):
        self.assertEqual(first_even([1, 3, 5]), -1)
        self.assertEqual(first_even([5, 7]), -1)
