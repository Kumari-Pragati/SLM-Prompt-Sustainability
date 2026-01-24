import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Number(10, 5), 5)

    def test_edge_case(self):
        self.assertEqual(get_Number(10, 1), 1)
        self.assertEqual(get_Number(10, 10), 10)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            get_Number(10, 11)

    def test_edge_case_with_zero(self):
        with self.assertRaises(IndexError):
            get_Number(0, 1)

    def test_edge_case_with_negative(self):
        with self.assertRaises(IndexError):
            get_Number(-1, 1)
