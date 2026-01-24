import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):
    def test_interleave_lists_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])

    def test_interleave_lists_single_element_lists(self):
        self.assertEqual(interleave_lists([1], [2], [3]), [1, 2, 3])

    def test_interleave_lists_multiple_element_lists(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 9])

    def test_interleave_lists_lists_of_different_lengths(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5], [6, 7, 8, 9]), [1, 4, 6, 2, 5, 7, 3, 8, 9])

    def test_interleave_lists_lists_with_duplicates(self):
        self.assertEqual(interleave_lists([1, 2, 2], [3, 4, 4], [5, 6, 6]), [1, 3, 5, 2, 4, 6, 2, 4, 6])
