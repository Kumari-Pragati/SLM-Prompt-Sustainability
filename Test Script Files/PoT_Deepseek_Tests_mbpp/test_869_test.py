import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 2, 6), [[2, 4], [4, 6]])

    def test_edge_case_leftrange(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 1, 6), [[1, 2], [3, 4], [5, 6]])

    def test_edge_case_rightrange(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 2, 6), [[2, 4], [4, 6]])

    def test_boundary_case(self):
        self.assertEqual(remove_list_range([[2, 3], [4, 5], [6, 7]], 3, 7), [[3, 5], [5, 7]])

    def test_corner_case_empty_list(self):
        self.assertEqual(remove_list_range([], 1, 10), [])

    def test_corner_case_single_element_list(self):
        self.assertEqual(remove_list_range([[1, 2]], 1, 2), [[1, 2]])

    def test_corner_case_single_element_out_of_range(self):
        self.assertEqual(remove_list_range([[1, 2]], 3, 4), [])

    def test_corner_case_single_element_in_range(self):
        self.assertEqual(remove_list_range([[1, 2]], 1, 3), [[1, 2]])
