import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_typical_case(self):
        arr = [4, 2, 9, 6, 23, 12, 34, 11]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [34, 23, 12, 11, 9, 6, 4, 2])

    def test_edge_case_start(self):
        arr = [4, 2, 9, 6, 23, 12, 34, 11]
        shift_down(arr, 0, 1)
        self.assertEqual(arr, [34, 23, 12, 11, 9, 6, 4, 2])

    def test_edge_case_end(self):
        arr = [4, 2, 9, 6, 23, 12, 34, 11]
        shift_down(arr, 0, len(arr) - 2)
        self.assertEqual(arr, [34, 23, 12, 11, 9, 6, 4, 2])

    def test_edge_case_root(self):
        arr = [4, 2, 9, 6, 23, 12, 34, 11]
        shift_down(arr, 0, 1)
        self.assertEqual(arr, [34, 23, 12, 11, 9, 6, 4, 2])

    def test_edge_case_child(self):
        arr = [4, 2, 9, 6, 23, 12, 34, 11]
        shift_down(arr, 0, 1)
        self.assertEqual(arr, [34, 23, 12, 11, 9, 6, 4, 2])

    def test_edge_case_no_child(self):
        arr = [4, 2, 9, 6, 23, 12, 34, 11]
        shift_down(arr, 0, 0)
        self.assertEqual(arr, [34, 23, 12, 11, 9, 6, 4, 2])
