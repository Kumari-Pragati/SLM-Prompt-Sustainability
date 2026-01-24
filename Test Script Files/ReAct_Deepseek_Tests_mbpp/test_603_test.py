import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_ludic(10), [1, 4, 7, 10])

    def test_single_ludic(self):
        self.assertEqual(get_ludic(1), [1])

    def test_no_ludic(self):
        self.assertEqual(get_ludic(0), [])

    def test_large_number(self):
        self.assertEqual(get_ludic(20), [1, 4, 7, 10, 13, 16, 19])

    def test_negative_number(self):
        with self.assertRaises(IndexError):
            get_ludic(-5)

    def test_large_number_with_many_ludics(self):
        self.assertEqual(get_ludic(30), [1, 4, 7, 10, 13, 16, 19, 22, 25, 28])
