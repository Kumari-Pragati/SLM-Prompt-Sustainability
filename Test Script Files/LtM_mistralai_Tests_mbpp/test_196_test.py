import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_simple_list_no_tuples(self):
        self.assertListEqual(remove_tuples([1, 2, 3, 4], 4), [1, 2, 3, 4])

    def test_simple_list_with_tuples(self):
        self.assertListEqual(remove_tuples([(1, 2), 3, 4], 4), [3, 4])

    def test_empty_list(self):
        self.assertListEqual(remove_tuples([], 4), [])

    def test_list_with_one_tuple(self):
        self.assertListEqual(remove_tuples([(1, 2)], 4), [])

    def test_list_with_one_tuple_and_other_elements(self):
        self.assertListEqual(remove_tuples([(1, 2), 3], 4), [3])

    def test_list_with_only_tuples(self):
        self.assertListEqual(remove_tuples([(1, 2), (3, 4)], 4), [])

    def test_list_with_tuples_of_different_lengths(self):
        self.assertListEqual(remove_tuples([(1, 2), (3, 4, 5), (6, 7)], 3), [(3, 4, 5)])

    def test_list_with_tuples_of_different_lengths_and_other_elements(self):
        self.assertListEqual(remove_tuples([(1, 2), (3, 4, 5), (6, 7), 8], 3), [8])
