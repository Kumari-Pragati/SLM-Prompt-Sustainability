import unittest
from mbpp_943_code import merge
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_combine_lists(self):
        self.assertEqual(combine_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(combine_lists([], []), [])
        self.assertEqual(combine_lists([1], []), [1])
        self.assertEqual(combine_lists([], [2]), [2])
        self.assertEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(combine_lists([7, 8, 9], [10, 11, 12]), [7, 8, 9, 10, 11, 12])
        self.assertEqual(combine_lists([1, 2, 3], [3, 2, 1]), [1, 1, 2, 2, 3, 3])
