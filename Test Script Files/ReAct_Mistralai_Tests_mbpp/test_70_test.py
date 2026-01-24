import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_same_length_list_of_tuples(self):
        input_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertEqual(get_equal(input_list, 3), "All tuples have same length")

    def test_different_length_list_of_tuples(self):
        input_list = [(1, 2, 3), (4, 5), (7, 8, 9)]
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")

    def test_empty_list(self):
        input_list = []
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")

    def test_single_tuple(self):
        input_list = [(1, 2, 3)]
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")

    def test_list_with_single_tuple_of_wrong_length(self):
        input_list = [(1, 2, 3, 4)]
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")

    def test_list_with_tuples_of_wrong_length(self):
        input_list = [(1, 2), (3, 4, 5), (6, 7, 8)]
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")
