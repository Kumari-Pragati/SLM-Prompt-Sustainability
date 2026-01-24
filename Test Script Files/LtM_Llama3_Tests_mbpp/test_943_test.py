import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(combine_lists([], []), [])

    def test_single_list(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])

    def test_reverse_order(self):
        self.assertEqual(combine_lists([3, 2, 1], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_mixed_order(self):
        self.assertEqual(combine_lists([3, 2, 1], [6, 5, 4]), [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        self.assertEqual(combine_lists([1, 2, 2, 3], [2, 4, 5]), [1, 2, 2, 3, 4, 5])

    def test_empty_input(self):
        self.assertEqual(combine_lists([], [1, 2, 3]), [1, 2, 3])

    def test_empty_output(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])
