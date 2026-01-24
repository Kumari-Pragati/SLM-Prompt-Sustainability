import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_ludic(10), [1, 4, 7, 10])

    def test_single_ludic(self):
        self.assertEqual(get_ludic(1), [1])

    def test_zero_ludics(self):
        self.assertEqual(get_ludic(0), [])

    def test_large_number(self):
        self.assertEqual(len(get_ludic(100)), 100)

    def test_negative_number(self):
        with self.assertRaises(IndexError):
            get_ludic(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            get_ludic(1.5)
