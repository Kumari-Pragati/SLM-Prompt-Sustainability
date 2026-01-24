import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4), (None, None)]
        expected_output = '[(1, 2), (3, 4)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_all_none_tuples(self):
        test_list = [(None, None), (None, None), (None, None)]
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_mixed_none_and_valid_tuples(self):
        test_list = [(1, 2), (None, None), (3, 4), (None, None)]
        expected_output = '[(1, 2), (3, 4)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_single_tuple(self):
        test_list = [(1, 2)]
        expected_output = '[(1, 2)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_single_none_tuple(self):
        test_list = [(None, None)]
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)
