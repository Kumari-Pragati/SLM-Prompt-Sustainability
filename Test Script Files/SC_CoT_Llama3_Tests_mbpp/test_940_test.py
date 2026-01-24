import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):
    def test_typical_input(self):
        arr = [5, 2, 8, 6, 1, 3, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 8])

    def test_edge_case(self):
        arr = [1, 2, 3, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_edge_case2(self):
        arr = [1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    def test_edge_case3(self):
        arr = []
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_edge_case4(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_invalid_input(self):
        arr = "Hello, World!"
        with self.assertRaises(TypeError):
            shift_down(arr, 0, len(arr) - 1)
