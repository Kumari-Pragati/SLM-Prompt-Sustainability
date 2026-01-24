import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 4)
        self.assertEqual(get_Number(5, 4), 6)
        self.assertEqual(get_Number(5, 5), 8)

    def test_odd_numbers(self):
        self.assertEqual(get_Number(10, 1), 1)
        self.assertEqual(get_Number(10, 2), 3)
        self.assertEqual(get_Number(10, 3), 5)
        self.assertEqual(get_Number(10, 4), 7)
        self.assertEqual(get_Number(10, 5), 9)
        self.assertEqual(get_Number(10, 6), 11)
        self.assertEqual(get_Number(10, 7), 13)
        self.assertEqual(get_Number(10, 8), 15)
        self.assertEqual(get_Number(10, 9), 17)
        self.assertEqual(get_Number(10, 10), 19)

    def test_even_numbers(self):
        self.assertEqual(get_Number(10, 11), 20)
        self.assertEqual(get_Number(10, 12), 18)
        self.assertEqual(get_Number(10, 13), 16)
        self.assertEqual(get_Number(10, 14), 14)
        self.assertEqual(get_Number(10, 15), 12)
        self.assertEqual(get_Number(10, 16), 10)
        self.assertEqual(get_Number(10, 17), 8)
        self.assertEqual(get_Number(10, 18), 6)
        self.assertEqual(get_Number(10, 19), 4)
        self.assertEqual(get_Number(10, 20), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(IndexError):
            get_Number(5, 0)
        with self.assertRaises(IndexError):
            get_Number(5, 6)
        with self.assertRaises(IndexError):
            get_Number(5, -1)
        with self.assertRaises(IndexError):
            get_Number(0, 1)
