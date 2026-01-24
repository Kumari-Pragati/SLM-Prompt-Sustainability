import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_max_of_two_positive_numbers(self):
        self.assertEqual(max_of_two(5, 3), 5)

    def test_max_of_two_negative_numbers(self):
        self.assertEqual(max_of_two(-5, -3), -3)

    def test_max_of_two_equal_numbers(self):
        self.assertEqual(max_of_two(5, 5), 5)

    def test_max_of_two_zero(self):
        self.assertEqual(max_of_two(0, 0), 0)

    def test_max_of_two_negative_zero(self):
        self.assertEqual(max_of_two(-0, -0), -0)

    def test_max_of_two_non_numeric_input(self):
        with self.assertRaises(TypeError):
            max_of_two('a', 'b')

    def test_max_of_two_mixed_type_input(self):
        with self.assertRaises(TypeError):
            max_of_two(5, 'b')

    def test_max_of_two_mixed_type_input2(self):
        with self.assertRaises(TypeError):
            max_of_two('a', 5)
