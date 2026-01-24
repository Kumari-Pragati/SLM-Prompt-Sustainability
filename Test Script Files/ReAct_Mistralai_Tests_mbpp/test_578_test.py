import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])
        self.assertEqual(interleave_lists([], [], [1]) , [])
        self.assertEqual(interleave_lists([], [1], []), [])
        self.assertEqual(interleave_lists([], [1, 2], [3, 4]), [1, 3])
        self.assertEqual(interleave_lists([1], [], [2, 3]), [1, 2, 3])
        self.assertEqual(interleave_lists([1, 2], [], [3, 4]), [1, 3, 2, 4])

    def test_single_list(self):
        self.assertEqual(interleave_lists([1], [], []), [1])
        self.assertEqual(interleave_lists([], [1], []), [1])
        self.assertEqual(interleave_lists([], [], [1]), [1])

    def test_lists_of_different_lengths(self):
        self.assertEqual(interleave_lists([1, 2], [3], [4, 5]), [1, 3, 2, 4])
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5]), [1, 3, 2, 4, 5])
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5, 6]), [1, 3, 2, 4, 5, 6])
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5, 6, 7]), [1, 3, 2, 4, 5, 6, 7])

    def test_lists_with_duplicates(self):
        self.assertEqual(interleave_lists([1, 1, 2], [3, 3], [4, 4]), [1, 3, 1, 4, 2, 3, 1, 4])
        self.assertEqual(interleave_lists([1, 2, 2], [3, 3], [4, 4]), [1, 3, 2, 4, 2, 3, 2, 4])
        self.assertEqual(interleave_lists([1, 2, 2], [3, 4], [4, 4]), [1, 3, 2, 4, 2, 4, 2, 4])
        self.assertEqual(interleave_lists([1, 2, 2], [3, 4, 4], [4, 4]), [1, 3, 2, 4, 2, 4, 2, 4])

    def test_lists_with_negative_numbers(self):
        self.assertEqual(interleave_lists([-1, 2], [-3, 3], [-4, 4]), [-1, -3, 2, 3, -4, 4])
        self.assertEqual(interleave_lists([-1, 2], [-3, 3, 3], [-4, 4]), [-1, -3, 2, 3, 3, -4, 4])
        self.assertEqual(interleave_lists([-1, 2], [-3, 4], [-4, 4]), [-1, -3, 2, 4, -4, 4])
        self.assertEqual(interleave_lists([-1, 2], [-3, 4, 4], [-4, 4]), [-1, -3, 2, 4, 4, -4, 4])

    def test_lists_with_floats(self):
        self.assertEqual(interleave_lists([1.1, 2], [3, 3], [4, 4]), [1.1, 3, 2, 4, 4])
        self.assertEqual(interleave_lists([1.1, 2], [3, 3.3], [4, 4]), [1.1, 3, 2, 3.3,