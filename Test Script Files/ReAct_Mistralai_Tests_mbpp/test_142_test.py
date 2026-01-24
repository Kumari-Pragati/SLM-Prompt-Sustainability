import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):

    def test_same_length_lists(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3], [3, 2, 1]), 3)
        self.assertEqual(count_samepair([4, 4, 4], [4, 4, 4], [4, 4, 4]), 3)
        self.assertEqual(count_samepair([5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]), 4)

    def test_different_length_lists(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3, 4], [3, 2, 1, 4]), 2)
        self.assertEqual(count_samepair([1, 2, 3, 4], [2, 1, 3], [3, 2, 1]), 1)
        self.assertEqual(count_samepair([1, 2, 3, 4], [2, 1, 3, 4, 5], [3, 2, 1, 4, 5]), 2)

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [], [1]), 1)
        self.assertEqual(count_samepair([1], [1], []), 1)
        self.assertEqual(count_samepair([], [1], [1]), 0)

    def test_lists_with_different_elements(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [4, 5, 6]), 0)

    def test_lists_with_duplicates(self):
        self.assertEqual(count_samepair([1, 1, 2, 2, 3], [1, 1, 2, 2, 3], [1, 1, 2, 2, 3]), 4)
        self.assertEqual(count_samepair([1, 1, 2, 2, 3], [1, 1, 2, 3, 2], [1, 1, 2, 3, 2]), 3)
        self.assertEqual(count_samepair([1, 1, 2, 2, 3], [1, 2, 2, 3, 1], [1, 2, 2, 3, 1]), 3)
