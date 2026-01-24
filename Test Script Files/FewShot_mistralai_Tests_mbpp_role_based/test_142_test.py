import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_same_length_lists(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([4, 5, 6], [5, 4, 6], [4, 5, 6]), 3)

    def test_different_length_lists(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3, 4], [1, 2, 3]), 2)
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3], [1, 2, 3, 4]), 0)

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [], [1]), 1)
        self.assertEqual(count_samepair([], [1], []), 0)

    def test_lists_with_duplicates(self):
        self.assertEqual(count_samepair([1, 1, 2], [2, 1, 1], [1, 2, 2]), 2)
        self.assertEqual(count_samepair([1, 1, 2, 2], [2, 1, 1, 2], [1, 2, 2, 1]), 2)
