import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_find_Min_Sum(self):
        self.assertEqual(find_Min_Sum([1, 4, 10, 6, 8], [1, 4, 10, 9, 10], 5), 3)
        self.assertEqual(find_Min_Sum([3, 2, 5, 2, 5, 2], [5, 6, 7, 8, 9, 0], 6), 9)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5), 10)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0), 0)
