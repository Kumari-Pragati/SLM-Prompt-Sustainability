import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_tuples([], 1), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_tuples([1], 1), [1])
        self.assertListEqual(remove_tuples([(1, 2)], 1), [])
        self.assertListEqual(remove_tuples([1], 2), [])

    def test_list_with_tuples(self):
        self.assertListEqual(remove_tuples([1, (1, 2), 3], 1), [3])
        self.assertListEqual(remove_tuples([(1, 2), (3, 4), (5, 6)], 2), [(1, 2), (5, 6)])
        self.assertListEqual(remove_tuples([(1, 2), 3], 1), [3])

    def test_list_with_non_tuples(self):
        self.assertListEqual(remove_tuples([1, 2, 3], 1), [2, 3])
        self.assertListEqual(remove_tuples([1, (1, 2)], 2), [1])

    def test_negative_k(self):
        self.assertRaises(ValueError, remove_tuples, [(1, 2)], -1)
