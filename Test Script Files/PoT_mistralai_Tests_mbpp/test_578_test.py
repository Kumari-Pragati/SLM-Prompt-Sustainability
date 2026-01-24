import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_empty_lists(self):
        self.assertListEqual(interleave_lists([], [], []), [])

    def test_single_list(self):
        self.assertListEqual(interleave_lists([1, 2, 3], [], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(interleave_lists([], [4, 5, 6], [1, 2, 3]), [4, 5, 6, 1, 2, 3])
        self.assertListEqual(interleave_lists([], [], [1, 2, 3]), [])

    def test_lists_of_different_lengths(self):
        self.assertListEqual(interleave_lists([1, 2], [3, 4, 5], [6, 7]), [1, 3, 2, 6, 4, 5])
        self.assertListEqual(interleave_lists([1, 2, 3], [4], [5, 6]), [1, 4, 2, 5, 3, 6])
        self.assertListEqual(interleave_lists([1, 2, 3], [4, 5], []), [1, 4, 2, 5, 3])
