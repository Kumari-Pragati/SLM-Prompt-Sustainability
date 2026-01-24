import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_find_sum(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Sum([1, 2, 2, 3, 4, 4, 5, 5], 5), 4)
        self.assertEqual(find_Sum([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5), 9)
        self.assertEqual(find_Sum([], 5), 0)
        self.assertEqual(find_Sum([1], 5), 0)
        self.assertEqual(find_Sum([1, 2], 5), 0)
        self.assertEqual(find_Sum([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], 6, ), 12)
