import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_volume(5), 60)

    def test_smallest_possible_case(self):
        self.assertEqual(max_volume(1), 0)

    def test_largest_possible_case(self):
        self.assertEqual(max_volume(100), 49999)

    def test_edge_case_zero(self):
        self.assertEqual(max_volume(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            max_volume(-1)

    def test_edge_case_large_number(self):
        with self.assertRaises(ValueError):
            max_volume(10000)
