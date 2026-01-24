import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(10, 2), 10)
        self.assertEqual(max_of_two(1, 0), 1)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(max_of_two(0, 5), 5)
        self.assertEqual(max_of_two(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_of_two(-3, -5), -3)
        self.assertEqual(max_of_two(-2, -7), -2)

    def test_edge_cases(self):
        self.assertEqual(max_of_two(2147483647, 2147483646), 2147483647)
        self.assertEqual(max_of_two(-2147483648, -2147483649), -2147483648)
        self.assertEqual(max_of_two(2147483647, -2147483648), 2147483647)
        self.assertEqual(max_of_two(-2147483648, 2147483647), -2147483648)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, max_of_two, 'a', 5)
        self.assertRaises(TypeError, max_of_two, 5, 'a')
        self.assertRaises(TypeError, max_of_two, 'a', 'b')
