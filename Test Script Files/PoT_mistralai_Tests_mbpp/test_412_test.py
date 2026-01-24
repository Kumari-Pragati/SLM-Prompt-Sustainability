import unittest
from412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])
        self.assertListEqual(remove_odd([-1, -2, -3, -4, -5]), [-2, -4])
        self.assertListEqual(remove_odd([0]), [])

    def test_edge_case_empty_list(self):
        self.assertListEqual(remove_odd([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(remove_odd([1]), [])
        self.assertListEqual(remove_odd([-1]), [])

    def test_corner_case_negative_numbers(self):
        self.assertListEqual(remove_odd([-1, 0, 1]), [-1, 1])
        self.assertListEqual(remove_odd([-1, -2, 0, 2]), [-1, -2])
        self.assertListEqual(remove_odd([-1, 0, 1, 2]), [-1, 1])
