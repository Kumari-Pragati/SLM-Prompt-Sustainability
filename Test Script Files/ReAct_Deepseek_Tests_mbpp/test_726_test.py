import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 6, 12))

    def test_single_element(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_empty_tuple(self):
        self.assertEqual(multiply_elements(()), ())

    def test_negative_numbers(self):
        self.assertEqual(multiply_elements((-1, 2, -3, 4)), (-2, -6, 12))

    def test_zero(self):
        self.assertEqual(multiply_elements((0, 2, 3, 4)), (0, 0, 0))

    def test_large_numbers(self):
        self.assertEqual(multiply_elements((1000, 2000, 3000)), (2000000, 6000000))

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            multiply_elements((1, 2.5, 3, 4))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            multiply_elements([1, 2, 3, 4])
