import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [], [1]), 1)
        self.assertEqual(count_samepair([1], [1], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(count_samepair([1], [2], [3]), 0)
        self.assertEqual(count_samepair([1], [1], [2]), 0)
        self.assertEqual(count_samepair([1], [1], [1]), 1)

    def test_equal_lists(self):
        self.assertEqual(count_samepair([1, 1], [1, 1], [1, 1]), 2)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 4], [1, 2, 3]), 2)

    def test_unequal_lists(self):
        self.assertEqual(count_samepair([1, 1], [2, 2], [3, 3]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [2, 3, 4], [1, 2, 5]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 4], [1, 2, 5]), 0)
