import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2, 3), (None, 2, None), (None, None, None)]
        expected_output = '[(1, 2, 3), (None, 2, None)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_all_none_tuples(self):
        test_list = [(None, None, None), (None, None, None), (None, None, None)]
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_mixed_tuples(self):
        test_list = [(1, 2, 3), (None, 2, None), (4, 5, 6), (None, None, None)]
        expected_output = '[(1, 2, 3), (None, 2, None), (4, 5, 6)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_single_tuple(self):
        test_list = [(1, 2, 3)]
        expected_output = '[(1, 2, 3)]'
        self.assertEqual(remove_tuple(test_list), expected_output)

    def test_single_none_tuple(self):
        test_list = [(None, None, None)]
        expected_output = '[]'
        self.assertEqual(remove_tuple(test_list), expected_output)
