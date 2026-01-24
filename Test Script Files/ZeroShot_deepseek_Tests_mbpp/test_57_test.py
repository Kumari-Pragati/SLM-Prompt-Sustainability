import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_find_Max_Num(self):
        self.assertEqual(find_Max_Num([3, 30, 34, 5, 9], 5), 9534330)
        self.assertEqual(find_Max_Num([54, 546, 548, 60], 4), 60548546544)
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)
        self.assertEqual(find_Max_Num([0, 0, 0, 0, 0], 5), 0)
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5], 5), 98765)
