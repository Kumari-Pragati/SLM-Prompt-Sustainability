import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_valid_index(self):
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(10, 5), 6)
        self.assertEqual(get_Number(20, 11), 19)

    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            get_Number(5, 6)
        with self.assertRaises(IndexError):
            get_Number(0, 1)
        with self.assertRaises(IndexError):
            get_Number(1, 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            get_Number(0, 1)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            get_Number(-1, 1)

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            get_Number(5, -1)
