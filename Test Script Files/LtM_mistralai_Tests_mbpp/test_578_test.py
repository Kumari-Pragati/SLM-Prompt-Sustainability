import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])
        self.assertListEqual(interleave_lists([], [], []), [])
        self.assertListEqual(interleave_lists([1], [], [2]), [1, 2])
        self.assertListEqual(interleave_lists([1], [2], []), [1, 2])

    def test_edge_cases(self):
        self.assertListEqual(interleave_lists([1], [2, 3], [4]), [1, 2, 4])
        self.assertListEqual(interleave_lists([1, 2], [3], [4]), [1, 3, 2, 4])
        self.assertListEqual(interleave_lists([1, 2], [3, 4], []), [1, 3, 2, 4])
        self.assertListEqual(interleave_lists([1, 2], [3, 4], [5, 6]), [1, 3, 2, 4, 5, 6])
        self.assertListEqual(interleave_lists([1, 2], [], [3, 4]), [1, 2, 3, 4])

    def test_complex(self):
        self.assertListEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]), [1, 4, 2, 5, 3, 6, 7, 8, 9, 10])
        self.assertListEqual(interleave_lists([1, 2, 3], [4, 5], [6, 7, 8]), [1, 4, 2, 5, 3, 6, 7, 8])
        self.assertListEqual(interleave_lists([1, 2], [3, 4, 5], [6, 7]), [1, 3, 2, 4, 5, 6, 7])
        self.assertListEqual(interleave_lists([1, 2], [3], [4, 5, 6]), [1, 3, 2, 4, 5, 6])
        self.assertListEqual(interleave_lists([1], [2, 3], [4, 5]), [1, 2, 3, 4, 5])
        self.assertListEqual(interleave_lists([1], [2], [3, 4]), [1, 2, 3, 4])
