import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_single_element(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_zero(self):
        self.assertEqual(multiply_list([0, 1, 2, 3]), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, 2, 3, -4]), -24)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            multiply_list([])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            multiply_list([1, 2, '3', 4])
