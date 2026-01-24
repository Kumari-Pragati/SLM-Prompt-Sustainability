import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_edge_case_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])

    def test_edge_case_single_list(self):
        self.assertEqual(interleave_lists([1], [], [3]), [1])
        self.assertEqual(interleave_lists([], [4], [5]), [4])
        self.assertEqual(interleave_lists([6], [], [7]), [6])

    def test_edge_case_lists_of_different_lengths(self):
        self.assertEqual(interleave_lists([1, 2], [3], [4, 5]), [1, 3, 2, 4])
        self.assertEqual(interleave_lists([1, 2], [3, 4], [5]), [1, 3, 2, 4, 5])
        self.assertEqual(interleave_lists([1], [2, 3], [4]), [1, 2, 3, 4])

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, interleave_lists, 1, 2, 3)
        self.assertRaises(TypeError, interleave_lists, [1], 'str', [3])
        self.assertRaises(TypeError, interleave_lists, [1], [2], 'str')
