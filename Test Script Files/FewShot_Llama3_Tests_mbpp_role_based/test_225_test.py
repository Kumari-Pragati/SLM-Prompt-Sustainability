import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_low_equal_high(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_high_equal_low(self):
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 5)

    def test_edge_case_low_greater_high(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_high_less_low(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_invalid_input_type(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            find_Min(arr, 'low', 'high')

    def test_invalid_input_value(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            find_Min(arr, -1, len(arr) - 1)
