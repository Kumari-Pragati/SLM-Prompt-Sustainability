import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_get_Number(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 4)
        self.assertEqual(get_Number(5, 4), 6)
        self.assertEqual(get_Number(5, 5), 8)

        self.assertEqual(get_Number(10, 1), 1)
        self.assertEqual(get_Number(10, 2), 2)
        self.assertEqual(get_Number(10, 3), 4)
        self.assertEqual(get_Number(10, 4), 6)
        self.assertEqual(get_Number(10, 5), 8)
        self.assertEqual(get_Number(10, 6), 10)
        self.assertEqual(get_Number(10, 7), 12)
        self.assertEqual(get_Number(10, 8), 14)
        self.assertEqual(get_Number(10, 9), 16)
        self.assertEqual(get_Number(10, 10), 18)

        with self.assertRaises(IndexError):
            get_Number(5, 0)
        with self.assertRaises(IndexError):
            get_Number(5, 6)
