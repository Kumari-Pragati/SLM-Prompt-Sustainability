import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_get_ludic_with_small_numbers(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(3), [1, 3])

    def test_get_ludic_with_large_numbers(self):
        self.assertEqual(get_ludic(10), [1, 3, 5, 7, 9])
        self.assertEqual(get_ludic(20), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_get_ludic_with_zero(self):
        self.assertEqual(get_ludic(0), [])

    def test_get_ludic_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            get_ludic(-1)
