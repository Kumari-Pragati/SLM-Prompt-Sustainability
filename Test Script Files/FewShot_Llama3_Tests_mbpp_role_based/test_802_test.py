import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [5, 2, 8, 2, 4]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 1)

    def test_edge_case_no_rotation(self):
        arr = [5, 2, 2, 4]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 0)

    def test_edge_case_first_element_is_smallest(self):
        arr = [5, 2, 1, 4]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 2)

    def test_edge_case_first_element_is_largest(self):
        arr = [5, 8, 2, 4]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 1)

    def test_edge_case_array_with_duplicates(self):
        arr = [5, 2, 2, 4, 2]
        n = len(arr)
        self.assertEqual(count_Rotation(arr, n), 1)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            count_Rotation(arr, n)
