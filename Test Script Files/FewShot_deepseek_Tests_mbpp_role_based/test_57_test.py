import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [5, 7, 9, 3, 6]
        n = len(arr)
        self.assertEqual(find_Max_Num(arr, n), 97536)

    def test_edge_condition(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(find_Max_Num(arr, n), 0)

    def test_boundary_condition(self):
        arr = [9, 9]
        n = len(arr)
        self.assertEqual(find_Max_Num(arr, n), 99)

    def test_invalid_input(self):
        arr = [5, 7, 'a', 3, 6]
        n = len(arr)
        with self.assertRaises(TypeError):
            find_Max_Num(arr, n)
