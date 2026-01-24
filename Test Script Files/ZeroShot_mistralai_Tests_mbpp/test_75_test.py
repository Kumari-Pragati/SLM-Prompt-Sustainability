import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_tuples([], 3), '[]')

    def test_single_element(self):
        self.assertEqual(find_tuples([1], 3), '[]')
        self.assertEqual(find_tuples([3], 3), '[[3]]')
        self.assertEqual(find_tuples([6], 3), '[[6]]')

    def test_multiple_elements(self):
        self.assertEqual(find_tuples([1, 2, 3], 3), '[]')
        self.assertEqual(find_tuples([3, 6, 9], 3), '[[3, 6, 9]]')
        self.assertEqual(find_tuples([4, 8, 12], 4), '[[4, 8, 12]]')
        self.assertEqual(find_tuples([5, 10, 15], 5), '[[5, 10], [15]]')
