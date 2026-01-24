import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_all_same(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3)

    def test_no_same(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)

    def test_some_same(self):
        self.assertEqual(count_samepair([1, 1, 2], [1, 2, 2], [1, 2, 2]), 2)

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_lists_of_different_lengths(self):
        with self.assertRaises(IndexError):
            count_samepair([1, 2], [1, 2, 3], [1, 2, 3, 4])
