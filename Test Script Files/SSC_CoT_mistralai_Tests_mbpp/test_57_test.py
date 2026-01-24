import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Max_Num([123, 456, 789], 3), 789)
        self.assertEqual(find_Max_Num([10, 20, 30], 3), 30)
        self.assertEqual(find_Max_Num([9, 8, 7], 3), 7)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Max_Num([], 0), 0)
        self.assertEqual(find_Max_Num([0], 1), 0)
        self.assertEqual(find_Max_Num([9, 8, 7, 6], 4), 9876)
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5], 5), 98765)
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5, 4], 6), 987654)
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5, 4, 3], 7), 9876543)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_Max_Num, [1, 2, 3], 'invalid')
        self.assertRaises(TypeError, find_Max_Num, [1, 2, 3], 0.5)
