import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_find_max_num(self):
        self.assertEqual(find_Max_Num([3, 6, 9], 3), 963)
        self.assertEqual(find_Max_Num([1, 2, 3], 3), 321)
        self.assertEqual(find_Max_Num([5, 5, 5], 3), 555)
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5, ), 54321)
        self.assertEqual(find_Max_Num([10, 20, 30, 40, 50], 5), 50320)
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1023456789)
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 1111023456789)

    def test_find_max_num_edge_cases(self):
        self.assertEqual(find_Max_Num([1], 1), 1)
        self.assertEqual(find_Max_Num([1, 2], 2), 21)
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], 100)
