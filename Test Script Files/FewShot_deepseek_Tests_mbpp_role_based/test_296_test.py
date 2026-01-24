import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 9, 6, 4, 5, 8, 7, 3, 2]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 16)

    def test_edge_condition(self):
        arr = []
        n = 0
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_boundary_condition(self):
        arr = [1]
        n = 1
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4]
        n = -1
        with self.assertRaises(Exception):
            get_Inv_Count(arr, n)
