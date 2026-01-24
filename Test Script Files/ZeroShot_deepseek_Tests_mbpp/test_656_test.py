import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_find_Min_Sum(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 5)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5), 16)
        self.assertEqual(find_Min_Sum([10, 20, 30], [10, 20, 30], 3), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 0)
