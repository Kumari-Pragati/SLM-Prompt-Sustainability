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

    def test_even_numbers(self):
        self.assertEqual(get_Number(10, 6), 2)
        self.assertEqual(get_Number(10, 7), 4)
        self.assertEqual(get_Number(10, 8), 6)
        self.assertEqual(get_Number(10, 9), 8)
        self.assertEqual(get_Number(10, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(get_Number(0, 1), 0)
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)

    def test_out_of_range(self):
        with self.assertRaises(IndexError):
            get_Number(5, 0)
        with self.assertRaises(IndexError):
            get_Number(5, 6)
