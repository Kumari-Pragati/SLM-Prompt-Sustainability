import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_noOfways(5), 8)

    def test_boundary_condition_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_boundary_condition_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_boundary_condition_two(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_edge_condition_large_number(self):
        self.assertEqual(get_noOfways(30), 1346269)

    def test_invalid_input_negative_number(self):
        with self.assertRaises(Exception):
            get_noOfways(-5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(Exception):
            get_noOfways(5.5)
