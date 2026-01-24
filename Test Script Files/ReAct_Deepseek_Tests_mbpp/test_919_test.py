import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_single_element(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_zero_element(self):
        self.assertEqual(multiply_list([]), 1)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(multiply_list([1, -2, 3, -4]), -24)

    def test_zero_in_list(self):
        self.assertEqual(multiply_list([1, 2, 0, 4]), 0)

    def test_large_numbers(self):
        self.assertEqual(multiply_list([10**5, 10**5]), 10**10)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            multiply_list([1, 2.5, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            multiply_list(123)
