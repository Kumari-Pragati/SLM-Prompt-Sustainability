import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(count_odd([]), 0)

    def test_all_even_numbers(self):
        self.assertEqual(count_odd([2, 4, 6, 8]), 0)

    def test_all_odd_numbers(self):
        self.assertEqual(count_odd([1, 3, 5, 7, 9]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)

    def test_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)

    def test_large_numbers(self):
        self.assertEqual(count_odd([1000000001, 1000000003, 1000000005]), 3)

    def test_float_numbers(self):
        self.assertEqual(count_odd([1.1, 2.2, 3.3, 4.4]), 2)

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            count_odd(['1', '2', '3', '4', '5'])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            count_odd(None)
