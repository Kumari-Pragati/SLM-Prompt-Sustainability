import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_Max_Num([1, 2, 3], 3), 213)
        self.assertEqual(find_Max_Num([4, 5, 6], 3), 654)
        self.assertEqual(find_Max_Num([7, 8, 9], 3), 987)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Max_Num([], 0), 0)
        self.assertEqual(find_Max_Num([1], 1), 1)
        self.assertEqual(find_Max_Num([1, 2], 2), 21)
        self.assertEqual(find_Max_Num([1, 2, 3, 4], 4), 4661)
        self.assertEqual(find_Max_Num([9, 9, 9, 9], 4), 9999)

    def test_complex_scenarios(self):
        self.assertEqual(find_Max_Num([0, 0, 0, 1], 4), 1)
        self.assertEqual(find_Max_Num([1, 2, 3, 0], 4), 3210)
        self.assertEqual(find_Max_Num([1, 0, 2, 3], 4), 3210)
        self.assertEqual(find_Max_Num([1, 2, 0, 3], 4), 3210)
        self.assertEqual(find_Max_Num([1, 0, 0, 3], 4), 3003)
        self.assertEqual(find_Max_Num([1, 0, 0, 0, 3], 5), 30003)
