import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_find_Sum(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(find_Sum([10, 20, 30, 40, 50], 5), 150)
        self.assertEqual(find_Sum([-1, -2, -3, -4, -5], 5), -3)
        self.assertEqual(find_Sum([0, 0, 0, 0, 0], 5), 0)
