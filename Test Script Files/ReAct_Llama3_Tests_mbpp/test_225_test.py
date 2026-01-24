import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_equal(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_min_at_start(self):
        arr = [5, 2, 3, 4, 1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_min_at_end(self):
        arr = [5, 2, 3, 4, 5]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 5)

    def test_edge_case_min_at_middle(self):
        arr = [5, 2, 1, 4, 3]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_case_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_Min(arr, 0, len(arr) - 1)

    def test_edge_case_single_element_array(self):
        arr = [1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)
