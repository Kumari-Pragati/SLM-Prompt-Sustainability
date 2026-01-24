import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(count_samepair([1], [1], [1]), 1)
        self.assertEqual(count_samepair([1], [2], [3]), 0)

    def test_multiple_element_lists(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [3, 2, 1], [1, 2, 3]), 2)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [4, 5, 6]), 0)
