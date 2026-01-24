import unittest

from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), ((1*2, 2*3, 3*4)))

    def test_single_element(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_empty_tuple(self):
        self.assertEqual(multiply_elements(()), ())

    def test_large_tuple(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
        self.assertEqual(multiply_elements(test_tup), expected_result)

    def test_negative_numbers(self):
        self.assertEqual(multiply_elements((-1, 2, -3, 4)), ((-1*2, 2*-3, -3*4)))

    def test_zero(self):
        self.assertEqual(multiply_elements((0, 2, 3, 4)), ((0*2, 2*3, 3*4)))

    def test_float_numbers(self):
        self.assertEqual(multiply_elements((1.5, 2.5, 3.5, 4.5)), ((1.5*2.5, 2.5*3.5, 3.5*4.5)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply_elements((1, 'a', 3, 4))
