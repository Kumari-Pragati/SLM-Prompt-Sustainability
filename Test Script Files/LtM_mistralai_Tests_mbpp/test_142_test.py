import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3], [3, 2, 1]), 2)
        self.assertEqual(count_samepair([4, 4, 4], [4, 4, 4], [4, 4, 4]), 3)
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [1], []), 0)
        self.assertEqual(count_samepair([1], [], [1]), 0)

    def test_edge_cases(self):
        self.assertEqual(count_samepair([-10, -10, -10], [-10, -10, -10], [-10, -10, -10]), 3)
        self.assertEqual(count_samepair([1000000000, 1000000000, 1000000000], [1000000000, 1000000000, 1000000000], [1000000000, 1000000000, 1000000000]), 3)
        self.assertEqual(count_samepair([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]), 2)
        self.assertEqual(count_samepair([0, 0, 0], [0, 0, 0], [1, 1, 1]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [4, 5, 6]), 0)
