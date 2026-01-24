import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4], 4), 4231)

    def test_edge_boundary_conditions(self):
        self.assertEqual(find_Max_Num([0], 1), 0)
        self.assertEqual(find_Max_Num([9, 9, 9, 9], 4), 9999)
        self.assertEqual(find_Max_Num([1, 0, 0, 0, 0], 5), 1)
        self.assertEqual(find_Max_Num([-1, -2, -3, -4], 4), -1234)

    def test_more_complex_cases(self):
        self.assertEqual(find_Max_Num([5, 5, 5, 5], 4), 5555)
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5], 5), 98765)
