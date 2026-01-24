import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):
    def test_typical_case(self):
        arr = [3, 2, 1, 5, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertGreaterEqual(arr[0], arr[1])
        self.assertGreaterEqual(arr[0], arr[2])
        self.assertGreaterEqual(arr[0], arr[3])
        self.assertGreaterEqual(arr[0], arr[4])

    def test_edge_case(self):
        arr = [1]
        shift_down(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_boundary_case(self):
        arr = [3, 2, 1]
        shift_down(arr, 0, 2)
        self.assertGreaterEqual(arr[0], arr[1])
        self.assertGreaterEqual(arr[0], arr[2])

    def test_invalid_input(self):
        arr = [3, 2, 1, 5, 4]
        with self.assertRaises(ValueError):
            shift_down(arr, 0, -1)
