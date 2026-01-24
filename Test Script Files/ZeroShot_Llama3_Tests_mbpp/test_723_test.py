import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_count_same_pair(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 4]), 1)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 5]), 1)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 3, 3]), 2)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 3, 4]), 1)
        self.assertEqual(count_same_pair([1, 2, 3], [2, 2, 3]), 1)
        self.assertEqual(count_same_pair([1, 2, 3], [2, 3, 3]), 1)
        self.assertEqual(count_same_pair([1, 2, 3], [3, 3, 3]), 2)
        self.assertEqual(count_same_pair([1, 2, 3], [3, 4, 5]), 0)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3, 4]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3, 4, 5]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3, 4, 5, 6]), 3)
