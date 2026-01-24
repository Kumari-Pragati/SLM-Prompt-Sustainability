import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_simple_case(self):
        arr = [3, 2, 1, 5, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 2, 1, 4, 3])

    def test_edge_case_single_element(self):
        arr = [1]
        shift_down(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_boundary_case_empty_array(self):
        arr = []
        shift_down(arr, 0, -1)
        self.assertEqual(arr, [])

    def test_complex_case_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 2, 3, 4, 1])

    def test_complex_case_large_array(self):
        arr = [5, 4, 3, 2, 1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 4, 3, 2, 1])
