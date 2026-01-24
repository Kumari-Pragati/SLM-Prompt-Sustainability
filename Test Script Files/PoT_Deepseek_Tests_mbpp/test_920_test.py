import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (None, 3), (4, None), (None, None)]
        expected_output = '[(1, 2), (3, None), (4, None)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_edge_case_empty_list(self):
        test_list = []
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_boundary_case_all_none(self):
        test_list = [(None, None), (None, None), (None, None)]
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_corner_case_all_valid(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_output = '[(1, 2), (3, 4), (5, 6)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_corner_case_mixed_valid_and_none(self):
        test_list = [(1, 2), (None, 3), (5, None), (None, None)]
        expected_output = '[(1, 2), (3, None), (5, None)]'
        self.assertEqual(remove_tuple(test_list), expected_output)
