import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_edge_case_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_lists([1], (2, 3)), (2, 3, 1))

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], (4,)), (4, 1, 2, 3))

    def test_edge_case_list_and_tuple_of_same_length(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_edge_case_list_longer_than_tuple(self):
        self.assertEqual(add_lists([1, 2, 3, 4], (4, 5, 6)), (4, 5, 6, 1, 2, 3, 4))

    def test_edge_case_tuple_longer_than_list(self):
        self.assertEqual(add_lists([1, 2], (1, 2, 3, 4)), (1, 2, 3, 4, 1, 2))
