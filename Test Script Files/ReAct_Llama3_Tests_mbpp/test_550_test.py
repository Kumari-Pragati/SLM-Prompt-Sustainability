import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_edge_case_low(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, 0), 1)

    def test_edge_case_high(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_edge_case_equal(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 1)

    def test_mid_element_max(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 1, len(arr) - 1), 5)

    def test_left_half_max(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) // 2), 3)

    def test_right_half_max(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, len(arr) // 2, len(arr) - 1), 5)

    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_array_with_duplicates_and_low_equal_high(self):
        arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)
