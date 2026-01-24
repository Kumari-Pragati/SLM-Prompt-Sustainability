import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):
    def test_remove_tuples_empty_list(self):
        self.assertListEqual(remove_tuples([], 1), [])

    def test_remove_tuples_single_tuple(self):
        self.assertListEqual(remove_tuples([(1, 2, 3)], 1), [])

    def test_remove_tuples_multiple_tuples(self):
        self.assertListEqual(remove_tuples([(1, 2, 3), (4, 5, 6)], 3), [(1, 2, 3)])

    def test_remove_tuples_list_with_non_tuples(self):
        self.assertListEqual(remove_tuples([1, (2, 3), 4], 2), [1, 4])

    def test_remove_tuples_list_with_single_element_tuples(self):
        self.assertListEqual(remove_tuples([(1), (2)], 1), [])

    def test_remove_tuples_list_with_empty_tuples(self):
        self.assertListEqual(remove_tuples([(), (1, 2, 3)], 1), [(1, 2, 3)])
