import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])
        self.assertEqual(interleave_lists([], [], [1]) , [])
        self.assertEqual(interleave_lists([], [1], []), [])
        self.assertEqual(interleave_lists([], [1, 2], [3]), [1, 3])
        self.assertEqual(interleave_lists([1], [], [2]), [1, 2])
        self.assertEqual(interleave_lists([1, 2], [], [3]), [1, 3, 2])

    def test_single_element_lists(self):
        self.assertEqual(interleave_lists([1], [2], [3]), [1, 2, 3])
        self.assertEqual(interleave_lists([1], [2, 3], []), [1, 2, 3])
        self.assertEqual(interleave_lists([1], [], [2, 3]), [1, 2, 3])
        self.assertEqual(interleave_lists([1, 2], [3], []), [1, 3, 2])
        self.assertEqual(interleave_lists([1, 2], [3], [4]), [1, 3, 2, 4])

    def test_lists_of_different_lengths(self):
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5, 6]), [1, 3, 2, 4, 5, 6])
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5]), [1, 3, 2, 5])
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5, 6, 7]), [1, 3, 2, 4, 5, 6, 7])
        self.assertEqual(interleave_lists([1, 2], [3, 4, 5], [6]), [1, 3, 2, 4, 5, 6])

    def test_lists_with_duplicates(self):
        self.assertEqual(interleave_lists([1, 2, 2], [3, 4], [5]), [1, 3, 2, 4, 2, 5])
        self.assertEqual(interleave_lists([1, 2, 2], [3, 4], [5, 5]), [1, 3, 2, 4, 2, 5, 5])
        self.assertEqual(interleave_lists([1, 2, 2], [3, 4, 4], [5]), [1, 3, 2, 4, 2, 4, 5])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, interleave_lists, [1], 'str', [3])
        self.assertRaises(TypeError, interleave_lists, 'int', [2], [3])
        self.assertRaises(TypeError, interleave_lists, [1], [2], 'list')
