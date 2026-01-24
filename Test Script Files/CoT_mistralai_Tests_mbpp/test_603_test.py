import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_ludic(0), [])

    def test_single_element(self):
        self.assertEqual(get_ludic(1), [1])

    def test_small_list(self):
        self.assertEqual(get_ludic(3), [1, 2, 3])

    def test_large_list(self):
        large_list = list(range(1, 1001))
        result = get_ludic(large_list)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            get_ludic(-1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            get_ludic(0)
