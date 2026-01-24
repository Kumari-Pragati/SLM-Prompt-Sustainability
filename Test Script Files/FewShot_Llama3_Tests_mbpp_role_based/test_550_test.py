import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_edge_case_low_equal_high(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, 0), 1)

    def test_edge_case_high_equal_low(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, len(arr) - 1, len(arr) - 1), 5)

    def test_edge_case_low_greater_high(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, len(arr) - 1, 0), 5)

    def test_edge_case_high_less_low(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_array_with_single_element(self):
        arr = [5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)
