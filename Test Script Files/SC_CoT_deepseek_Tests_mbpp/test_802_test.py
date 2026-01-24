import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Rotation([15, 18, 2, 3, 6, 12], 6), 2)

    def test_edge_case_small_array(self):
        self.assertEqual(count_Rotation([2, 3, 6, 12, 15, 18], 6), 0)

    def test_edge_case_large_array(self):
        self.assertEqual(count_Rotation([15, 18, 2, 3, 6, 12, 15, 18, 2, 3, 6, 12], 12), 2)

    def test_corner_case_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_corner_case_empty_array(self):
        self.assertEqual(count_Rotation([], 0), 0)

    def test_invalid_input_negative_numbers(self):
        with self.assertRaises(Exception):
            count_Rotation([-1, -2, -3], 3)

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(Exception):
            count_Rotation([1, 2, 'a'], 3)
