import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_get_number_valid_input(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 1)
        self.assertEqual(get_Number(5, 4), 2)
        self.assertEqual(get_Number(5, 5), 3)
        self.assertEqual(get_Number(5, 6), 4)
        self.assertEqual(get_Number(5, 7), 5)

    def test_get_number_invalid_input(self):
        with self.assertRaises(IndexError):
            get_Number(5, 8)

    def test_get_number_invalid_n(self):
        with self.assertRaises(IndexError):
            get_Number(0, 1)

    def test_get_number_invalid_k(self):
        with self.assertRaises(IndexError):
            get_Number(5, 0)
