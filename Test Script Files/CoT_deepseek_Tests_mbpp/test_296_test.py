import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 9, 6, 4, 5, 0]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 5)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_sorted_array(self):
        arr = [0, 1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1, 0]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 15)

    def test_single_element_array(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_duplicate_elements(self):
        arr = [1, 3, 1, 2, 0, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 3)

    def test_negative_elements(self):
        arr = [-1, -3, -2, -4, -5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 10)

    def test_large_array(self):
        arr = list(range(10000, -1, -1))
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 49995000)
