import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_typical_case(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        expected = [1, 3, 2, 5, 4, 6, 8, 7, 9]
        self.assertEqual(shift_down(arr, 0, len(arr) - 1), None)
        self.assertEqual(arr, expected)

    def test_empty_list(self):
        arr = []
        self.assertEqual(shift_down(arr, 0, len(arr) - 1), None)
        self.assertEqual(arr, [])

    def test_single_element_list(self):
        arr = [3]
        self.assertEqual(shift_down(arr, 0, len(arr) - 1), None)
        self.assertEqual(arr, [3])

    def test_boundary_case_start_0(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        self.assertEqual(shift_down(arr, 0, 0), None)
        self.assertEqual(arr, [5, 3, 8, 6, 1, 9, 2, 7, 4])

    def test_boundary_case_end_1(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        self.assertEqual(shift_down(arr, 0, 1), None)
        self.assertEqual(arr, [3, 5, 8, 6, 1, 9, 2, 7, 4])

    def test_boundary_case_start_len(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        self.assertEqual(shift_down(arr, len(arr), len(arr) - 1), None)
        self.assertEqual(arr, [5, 3, 8, 6, 1, 9, 2, 7, 4])

    def test_boundary_case_end_len_1(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        self.assertEqual(shift_down(arr, len(arr) - 1, len(arr) - 1), None)
        self.assertEqual(arr, [5, 3, 8, 6, 1, 9, 2, 7, 4])

    def test_boundary_case_start_end(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        self.assertEqual(shift_down(arr, 0, 0), None)
        self.assertEqual(arr, [5, 3, 8, 6, 1, 9, 2, 7, 4])

    def test_negative_start(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        with self.assertRaises(IndexError):
            shift_down(arr, -1, len(arr) - 1)

    def test_negative_end(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        with self.assertRaises(IndexError):
            shift_down(arr, 0, -1)

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            shift_down(1.5, 0, len(arr) - 1)

        with self.assertRaises(TypeError):
            shift_down([1, 2, 3], 'start', len(arr) - 1)
