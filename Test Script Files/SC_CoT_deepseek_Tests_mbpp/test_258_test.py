import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(count_odd([]), 0)

    def test_all_even(self):
        self.assertEqual(count_odd([2, 4, 6, 8]), 0)

    def test_all_odd(self):
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6]), 3)

    def test_large_numbers(self):
        self.assertEqual(count_odd([i for i in range(1, 10001) if i % 2 != 0]), 5000)

    def test_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)

    def test_negative_even_numbers(self):
        self.assertEqual(count_odd([-2, -4, -6, -8]), 0)

    def test_negative_odd_numbers(self):
        self.assertEqual(count_odd([-1, -3, -5, -7]), 4)

    def test_mixed_negative_numbers(self):
        self.assertEqual(count_odd([-1, 2, -3, 4, -5, 6]), 3)

    def test_float_numbers(self):
        with self.assertRaises(TypeError):
            count_odd([1.0, 2.0, 3.0])

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            count_odd(['1', '2', '3'])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            count_odd(None)
