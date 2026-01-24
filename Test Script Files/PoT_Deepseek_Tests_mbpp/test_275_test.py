import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Position([10, 20, 30, 40], 4, 2), 2)

    def test_edge_case_with_single_element(self):
        self.assertEqual(get_Position([10], 1, 2), 1)

    def test_boundary_case_with_multiple_elements(self):
        self.assertEqual(get_Position([10, 20, 30, 40], 4, 1), 4)

    def test_corner_case_with_large_numbers(self):
        self.assertEqual(get_Position([10000, 20000, 30000, 40000], 4, 1000), 1)

    def test_corner_case_with_small_numbers(self):
        self.assertEqual(get_Position([1, 2, 3, 4], 4, 1), 4)

    def test_invalid_input_with_negative_numbers(self):
        with self.assertRaises(Exception):
            get_Position([-10, -20, -30, -40], 4, 2)

    def test_invalid_input_with_zero_division(self):
        with self.assertRaises(Exception):
            get_Position([10, 20, 30, 40], 4, 0)
