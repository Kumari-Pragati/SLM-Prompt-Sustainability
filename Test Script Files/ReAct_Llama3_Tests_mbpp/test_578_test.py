import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])

    def test_single_element_lists(self):
        self.assertEqual(interleave_lists([1], [2], [3]), [1, 2, 3])

    def test_lists_of_same_length(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 9])

    def test_lists_of_different_lengths(self):
        self.assertEqual(interleave_lists([1, 2, 3, 4], [5, 6], [7, 8, 9, 10]), [1, 5, 7, 2, 6, 8, 3, 9, 10, 4])

    def test_lists_with_duplicates(self):
        self.assertEqual(interleave_lists([1, 2, 2, 3], [4, 5, 5], [6, 7, 7]), [1, 4, 6, 2, 5, 7, 2, 5, 7, 3])

    def test_lists_with_empty_sublists(self):
        self.assertEqual(interleave_lists([1, 2], [], [3, 4]), [1, 3, 2, 4])
