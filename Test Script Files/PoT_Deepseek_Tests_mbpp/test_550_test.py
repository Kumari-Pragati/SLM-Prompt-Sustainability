import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 9], 0, 4), 9)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Max([5], 0, 0), 5)

    def test_boundary_case_two_elements(self):
        self.assertEqual(find_Max([5, 3], 0, 1), 5)

    def test_corner_case_descending_order(self):
        self.assertEqual(find_Max([9, 7, 5, 3, 1], 0, 4), 9)

    def test_corner_case_duplicate_max(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 7, 9], 0, 5), 9)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            find_Max([], -1, 0)
