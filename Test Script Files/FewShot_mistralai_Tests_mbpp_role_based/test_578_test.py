import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):
    def test_interleave_equal_length_lists(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_interleave_lists_with_different_lengths(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5], [6, 7, 8, 9]), [1, 4, 2, 5, 3, 6, 7, 8, 9])

    def test_interleave_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])

    def test_interleave_lists_with_one_element(self):
        self.assertEqual(interleave_lists([1], [2], [3]), [1, 2, 3])
        self.assertEqual(interleave_lists([1], [], [3]), [1, 3])
        self.assertEqual(interleave_lists([], [2], [3]), [2, 3])
