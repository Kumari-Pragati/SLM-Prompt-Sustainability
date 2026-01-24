import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_min_of_two_positive_numbers(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(2, 1), 1)

    def test_min_of_two_zero_and_positive_number(self):
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(1, 0), 0)

    def test_min_of_two_negative_numbers(self):
        self.assertEqual(min_of_two(-1, -2), -1)
        self.assertEqual(min_of_two(-2, -1), -1)

    def test_min_of_two_equal_numbers(self):
        self.assertEqual(min_of_two(-1, -1), -1)
        self.assertEqual(min_of_two(1, 1), 1)

    def test_min_of_two_invalid_input_non_numeric(self):
        self.assertRaises(TypeError, min_of_two, 'a', 'b')
        self.assertRaises(TypeError, min_of_two, 1, 'b')
        self.assertRaises(TypeError, min_of_two, 'a', 1)
