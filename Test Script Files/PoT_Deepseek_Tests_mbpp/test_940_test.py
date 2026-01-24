import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_typical_case(self):
        arr = [3, 2, 1, 5, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [2, 1, 3, 5, 4])

    def test_edge_case_single_element(self):
        arr = [1]
        shift_down(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_boundary_case_root_at_end(self):
        arr = [5, 4, 3, 2, 1]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_boundary_case_root_at_middle(self):
        arr = [5, 4, 3, 2, 1]
        shift_down(arr, 1, 4)
        self.assertEqual(arr, [4, 1, 3, 2, 5])

    def test_corner_case_large_array(self):
        arr = list(range(1000, 0, -1))
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, list(range(1, 1001)))
