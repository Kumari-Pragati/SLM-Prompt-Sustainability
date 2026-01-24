import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_typical_case(self):
        arr = [3, 2, 1, 5, 4]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [5, 2, 1, 3, 4])

    def test_single_element(self):
        arr = [1]
        shift_down(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [5, 2, 3, 4, 1])

    def test_negative_numbers(self):
        arr = [-3, -2, -1, -5, -4]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [-5, -2, -1, -3, -4])

    def test_large_numbers(self):
        arr = [100, 200, 300, 400, 500]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [500, 200, 300, 400, 100])

    def test_edge_case(self):
        arr = [5, 4, 3, 2, 1]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            shift_down("not a list", 0, 4)
