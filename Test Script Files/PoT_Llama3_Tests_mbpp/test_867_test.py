import unittest
from mbpp_867_code import min_Num

class TestMin_Num(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)

    def test_odd_numbers(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 1)

    def test_even_numbers(self):
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)

    def test_mixed_numbers(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)

    def test_single_element(self):
        self.assertEqual(min_Num([1], 1), 2)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            min_Num([], 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_Num("hello", 5)
