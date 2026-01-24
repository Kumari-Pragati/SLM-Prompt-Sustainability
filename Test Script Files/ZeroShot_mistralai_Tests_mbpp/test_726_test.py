import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(multiply_elements(()), tuple)
        self.assertEqual(multiply_elements(()), ())

    def test_single_element_tuple(self):
        self.assertIsInstance(multiply_elements((1,)), tuple)
        self.assertEqual(multiply_elements((1,)), ())

    def test_simple_tuple(self):
        self.assertIsInstance(multiply_elements((1, 2, 3)), tuple)
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 4, 6))

    def test_negative_numbers(self):
        self.assertIsInstance(multiply_elements((-1, 2, -3)), tuple)
        self.assertEqual(multiply_elements((-1, 2, -3)), (2, -4, 3))

    def test_zero(self):
        self.assertIsInstance(multiply_elements((0, 2, 3)), tuple)
        self.assertEqual(multiply_elements((0, 2, 3)), (0, 0, 0))
