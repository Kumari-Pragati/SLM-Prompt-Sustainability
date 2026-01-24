import unittest

from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(max_volume(5), 60)

    def test_edge_case_smallest_possible_input(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_case_largest_possible_input(self):
        self.assertEqual(max_volume(100), 75000)

    def test_corner_case_input_2(self):
        self.assertEqual(max_volume(2), 2)

    def test_invalid_input_negative_number(self):
        with self.assertRaises(ValueError):
            max_volume(-1)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            max_volume(0)
