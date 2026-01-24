import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])
        self.assertListEqual(remove_even([2, 4, 6]), [])
        self.assertListEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertListEqual(remove_even([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(remove_even([0]), [])
        self.assertListEqual(remove_even([1]), [1])

    def test_edge_case_negative_numbers(self):
        self.assertListEqual(remove_even([2, -2, 3, -3]), [3])
        self.assertListEqual(remove_even([-1, -2, -3]), [])
