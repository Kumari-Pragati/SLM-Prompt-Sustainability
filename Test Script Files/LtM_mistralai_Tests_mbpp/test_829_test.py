import unittest
from mbpp_829_code import Counter
from 829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 4)
        self.assertEqual(second_frequent([1, 1, 1, 2, 2, 2, 3, 3, 3, 4]), 3)
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4]), 2)

    def test_edge_cases(self):
        self.assertEqual(second_frequent([]), None)
        self.assertEqual(second_frequent([1]), None)
        self.assertEqual(second_frequent([1, 1]), None)
        self.assertEqual(second_frequent([1, 1, 1]), None)
        self.assertEqual(second_frequent([1, 1, 1, 2]), 1)
        self.assertEqual(second_frequent([1, 1, 1, 1, 2]), 2)
        self.assertEqual(second_frequent([1, 1, 1, 1, 1, 2]), 1)
        self.assertEqual(second_frequent([1, 1, 1, 1, 1, 1, 2]), None)
        self.assertEqual(second_frequent([2, 2, 2, 2, 2, 2, 2]), None)
