import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list([123, 45, 678]), "[45, 123, 678]")

    def test_edge_case_single_digit(self):
        self.assertEqual(sort_list([1, 2, 3]), "[1, 2, 3]")

    def test_edge_case_single_element(self):
        self.assertEqual(sort_list([123]), "[123]")

    def test_boundary_case_empty_list(self):
        self.assertEqual(sort_list([]), "[]")

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(sort_list([123, 45, 45]), "[45, 45, 123]")

    def test_corner_case_negative_numbers(self):
        self.assertEqual(sort_list([-123, -45, -678]), "[-678, -123, -45]")

    def test_corner_case_mixed_positive_negative(self):
        self.assertEqual(sort_list([123, -45, 678]), "[-45, 123, 678]")
