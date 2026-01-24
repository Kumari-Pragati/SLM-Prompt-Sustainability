import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):

    def test_count_samepair(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [1, 2, 3]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [4, 5, 6]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [1, 2, 3]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [4, 5, 6]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [1, 2, 3]), 0)
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [4, 5, 6]), 0)
