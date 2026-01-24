import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(bell_number(3), 5)

    def test_edge_case(self):
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            bell_number(-1)

    def test_edge_case_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_edge_case_large(self):
        self.assertEqual(bell_number(10), 5723)

    def test_edge_case_large_negative(self):
        with self.assertRaises(ValueError):
            bell_number(-10)

    def test_edge_case_large_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_edge_case_large_one(self):
        self.assertEqual(bell_number(1), 1)

    def test_edge_case_large_two(self):
        self.assertEqual(bell_number(2), 2)

    def test_edge_case_large_three(self):
        self.assertEqual(bell_number(3), 5)

    def test_edge_case_large_four(self):
        self.assertEqual(bell_number(4), 15)

    def test_edge_case_large_five(self):
        self.assertEqual(bell_number(5), 52)

    def test_edge_case_large_six(self):
        self.assertEqual(bell_number(6), 203)

    def test_edge_case_large_seven(self):
        self.assertEqual(bell_number(7), 676)

    def test_edge_case_large_eight(self):
        self.assertEqual(bell_number(8), 2578)

    def test_edge_case_large_nine(self):
        self.assertEqual(bell_number(9), 6765)

    def test_edge_case_large_ten(self):
        self.assertEqual(bell_number(10), 5723)
