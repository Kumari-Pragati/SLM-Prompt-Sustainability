import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_interleave_lists(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])
        self.assertEqual(interleave_lists([], [], []), [])
        self.assertEqual(interleave_lists([1], [2], [3]), [1, 2, 3])
        self.assertEqual(interleave_lists(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']), ['a', 'd', 'g', 'b', 'e', 'h', 'c', 'f', 'i'])
