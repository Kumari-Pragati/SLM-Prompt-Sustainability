import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(multiply_elements(()), tuple)
        self.assertIsInstance(multiply_elements((1,)), tuple)

    def test_single_element_tuple(self):
        self.assertIsInstance(multiply_elements((1,)), tuple)
        self.assertEqual(multiply_elements((1,)), ())

    def test_normal_case(self):
        self.assertIsInstance(multiply_elements((1, 2, 3, 4)), tuple)
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 4, 6, 8))

    def test_negative_numbers(self):
        self.assertIsInstance(multiply_elements((-1, 2, -3, 4)), tuple)
        self.assertEqual(multiply_elements((-1, 2, -3, 4)), (2, -4, -6, 4))

    def test_floats(self):
        self.assertIsInstance(multiply_elements((1.5, 2.5)), tuple)
        self.assertNotEqual(multiply_elements((1.5, 2.5)), (3.0, 5.0))

    def test_invalid_input(self):
        self.assertRaises(TypeError, multiply_elements, (1, 'a'))
        self.assertRaises(TypeError, multiply_elements, (1, [2, 3]))
