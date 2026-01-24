import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_tuples([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(remove_tuples([1], 1), [1])

    def test_list_with_single_tuple(self):
        self.assertEqual(remove_tuples([(1, 2)], 1), [])

    def test_list_with_multiple_tuples(self):
        self.assertEqual(remove_tuples([(1, 2), (3, 4), (5, 6)], 2), [(1, 2), (5, 6)])

    def test_list_with_non_tuple_elements(self):
        self.assertEqual(remove_tuples([1, (2, 3), 4], 2), [1, 4])

    def test_list_with_tuples_and_non_tuples(self):
        self.assertEqual(remove_tuples([1, (2, 3), 4, (5, 6)], 2), [1, 4])
