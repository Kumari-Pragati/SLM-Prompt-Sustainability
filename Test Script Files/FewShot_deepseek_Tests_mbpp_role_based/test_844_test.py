import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Number(10, 5), 4)

    def test_odd_position(self):
        self.assertEqual(get_Number(10, 1), 1)

    def test_even_position(self):
        self.assertEqual(get_Number(10, 2), 2)

    def test_large_number(self):
        self.assertEqual(get_Number(100, 50), 50)

    def test_boundary_conditions(self):
        self.assertEqual(get_Number(1, 1), 0)
        self.assertEqual(get_Number(2, 2), 2)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            get_Number(-10, 5)
        with self.assertRaises(Exception):
            get_Number(10, 0)
        with self.assertRaises(Exception):
            get_Number(10, 11)
