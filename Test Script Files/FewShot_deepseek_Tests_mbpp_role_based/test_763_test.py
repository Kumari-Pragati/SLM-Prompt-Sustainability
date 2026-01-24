import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 5, 3, 19, 18, 25]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 1)

    def test_edge_case_single_element(self):
        arr = [10]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 0)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 0)

    def test_invalid_input_non_integer_elements(self):
        arr = [1, 5, '3', 19, 18, 25]
        n = len(arr)
        with self.assertRaises(TypeError):
            find_Min_Diff(arr, n)

    def test_invalid_input_negative_elements(self):
        arr = [1, 5, -3, 19, 18, 25]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 2)
