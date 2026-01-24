import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_of_two(10, 20), 20)

    def test_reverse_order(self):
        self.assertEqual(max_of_two(20, 10), 20)

    def test_equal_numbers(self):
        self.assertEqual(max_of_two(10, 10), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_of_two(-10, -20), -10)

    def test_one_negative_number(self):
        self.assertEqual(max_of_two(-10, 20), 20)

    def test_zero(self):
        self.assertEqual(max_of_two(0, 20), 20)

    def test_large_numbers(self):
        self.assertEqual(max_of_two(1000000, 2000000), 2000000)

    def test_float_numbers(self):
        self.assertEqual(max_of_two(10.5, 20.5), 20.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            max_of_two("10", 20)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            max_of_two([10], 20)
