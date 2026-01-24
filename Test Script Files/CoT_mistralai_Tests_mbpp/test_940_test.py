import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(shift_down([]), None)

    def test_single_element(self):
        self.assertEqual(shift_down([1]), [1])

    def test_typical_case(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        expected = [1, 3, 5, 6, 8, 9, 2, 7, 4]
        self.assertEqual(shift_down(arr, 0, len(arr) - 1), None)
        self.assertEqual(arr, expected)

    def test_edge_case_start_equal_end(self):
        arr = [5]
        self.assertEqual(shift_down(arr, 0, 0), None)
        self.assertEqual(arr, [5])

    def test_edge_case_start_greater_than_end(self):
        arr = [5, 3, 8]
        self.assertEqual(shift_down(arr, 3, 2), None)
        self.assertEqual(arr, [5, 3, 8])

    def test_edge_case_root_not_a_node(self):
        arr = [5]
        self.assertEqual(shift_down(arr, -1, 0), None)
        self.assertEqual(arr, [5])

    def test_edge_case_root_is_a_leaf(self):
        arr = [5, 3]
        self.assertEqual(shift_down(arr, 1, 0), None)
        self.assertEqual(arr, [5, 3])

    def test_edge_case_child_out_of_bounds(self):
        arr = [5, 3]
        self.assertEqual(shift_down(arr, 0, -1), None)
        self.assertEqual(arr, [5, 3])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            shift_down('abc', 0, 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            shift_down([1], -1, 0)
