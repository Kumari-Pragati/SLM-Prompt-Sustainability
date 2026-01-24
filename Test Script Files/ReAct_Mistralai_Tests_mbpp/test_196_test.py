import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_tuples([], 1), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_tuples([1], 1), [1])
        self.assertListEqual(remove_tuples([(1,)], 1), [])
        self.assertListEqual(remove_tuples([(1,)], 2), [(1,)])

    def test_list_with_tuples_and_non_tuples(self):
        self.assertListEqual(remove_tuples([1, (1, 2), 3], 1), [3])
        self.assertListEqual(remove_tuples([1, (1, 2), 3], 2), [1, 3])
        self.assertListEqual(remove_tuples([(1, 2), (3, 4)], 2), [(1, 2), (3, 4)])

    def test_list_with_only_tuples(self):
        self.assertListEqual(remove_tuples([(1, 2), (3, 4)], 1), [(3, 4)])
        self.assertListEqual(remove_tuples([(1, 2), (3, 4)], 2), [])

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            remove_tuples([(1, 2)], -1)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            remove_tuples([], 0)
