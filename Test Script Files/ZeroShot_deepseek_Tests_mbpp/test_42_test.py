import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_find_Sum(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 5)
        self.assertEqual(find_Sum([1, 2, 2, 3, 3], 5), 4)
        self.assertEqual(find_Sum([], 0), 0)
