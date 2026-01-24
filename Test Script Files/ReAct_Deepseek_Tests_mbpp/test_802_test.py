import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_case(self):
        arr = [5, 6, 1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 2)

    def test_edge_case_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 0)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 0)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 0)

    def test_edge_case_duplicates(self):
        arr = [5, 5, 1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 3)

    def test_error_case_non_integer_input(self):
        arr = [5, 6, 1, 2, 3, 4]
        n = 'not an integer'
        with self.assertRaises(TypeError):
            count_Rotation(arr, n)

    def test_error_case_negative_index(self):
        arr = [5, 6, 1, 2, 3, 4]
        n = -1
        with self.assertRaises(ValueError):
            count_Rotation(arr, n)
