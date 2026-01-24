import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_find_Min_Sum(self):
        self.assertEqual(find_Min_Sum(12), 10)
        self.assertEqual(find_Min_Sum(15), 15)
        self.assertEqual(find_Min_Sum(100), 100)
        self.assertEqual(find_Min_Sum(101), 101)
        self.assertEqual(find_Min_Sum(102), 101)
        self.assertEqual(find_Min_Sum(103), 103)
        self.assertEqual(find_Min_Sum(104), 103)
        self.assertEqual(find_Min_Sum(105), 105)
        self.assertEqual(find_Min_Sum(106), 105)
        self.assertEqual(find_Min_Sum(107), 107)
