import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(multiply_elements(()), ())

    def test_single_element_input(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_two_element_input(self):
        self.assertEqual(multiply_elements((1, 2)), (1,))

    def test_three_element_input(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (1, 2))

    def test_four_element_input(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (1, 2, 6))

    def test_five_element_input(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5)), (1, 2, 6, 12))

    def test_negative_numbers(self):
        self.assertEqual(multiply_elements((-1, 2, 3, 4, 5)), (-1, -2, -6, -12))

    def test_zero_in_input(self):
        self.assertEqual(multiply_elements((0, 1, 2, 3, 4)), (0, 0, 0, 0))

    def test_large_numbers(self):
        self.assertEqual(multiply_elements((100, 200, 300, 400, 500)), (10000, 20000, 60000, 120000))
