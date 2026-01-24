import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_interleave_lists(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 9])
        self.assertEqual(interleave_lists([], [], []), [])
        self.assertEqual(interleave_lists([1, 2], [3, 4], []), [1, 3, 2, 4])
        self.assertEqual(interleave_lists([1, 2, 3], [], [4, 5, 6]), [1, 4, 2, 5, 3, 6])
        self.assertEqual(interleave_lists([1, 2], [], [3, 4, 5]), [1, 3, 2, 4, 5])

    def test_interleave_lists_empty_list(self):
        self.assertEqual(interleave_lists([], [], []), [])
        self.assertEqual(interleave_lists([1, 2], [], []), [])
        self.assertEqual(interleave_lists([], [1, 2], []), [])
        self.assertEqual(interleave_lists([], [], [1, 2]), [])
