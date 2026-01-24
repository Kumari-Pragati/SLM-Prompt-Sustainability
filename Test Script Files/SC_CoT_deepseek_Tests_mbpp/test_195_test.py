import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_edge_case_x_not_in_array(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case_empty_array(self):
        arr = []
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case_single_element_array(self):
        arr = [5]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_edge_case_all_elements_same(self):
        arr = [3, 3, 3, 3, 3]
        x = 3
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_invalid_input_negative_index(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = -1
        with self.assertRaises(IndexError):
            first(arr, x, n)

    def test_invalid_input_non_integer_index(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = 'a'
        with self.assertRaises(TypeError):
            first(arr, x, n)
