import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3)

    def test_empty(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [], []), 0)
        self.assertEqual(count_samepair([], [1], []), 0)
        self.assertEqual(count_samepair([], [], [1]), 0)

    def test_single(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([1, 1, 1], [1, 2, 3], [1, 2, 3]), 1)
        self.assertEqual(count_samepair([1, 2, 3], [1, 1, 1], [1, 2, 3]), 1)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 1, 1]), 1)

    def test_edge(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 2]), 2)
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 2], [1, 1, 1]), 2)
        self.assertEqual(count_samepair([1, 1, 1], [1, 2, 3], [1, 1, 1]), 1)
