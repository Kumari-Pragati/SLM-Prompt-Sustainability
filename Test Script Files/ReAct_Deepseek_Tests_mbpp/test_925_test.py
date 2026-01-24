import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mutiple_tuple((2, 3, 4)), 24)

    def test_single_element(self):
        self.assertEqual(mutiple_tuple((5,)), 5)

    def test_empty_tuple(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_negative_numbers(self):
        self.assertEqual(mutiple_tuple((-2, -3, 4)), -6)

    def test_zero_in_tuple(self):
        self.assertEqual(mutiple_tuple((2, 3, 0)), 0)

    def test_large_numbers(self):
        self.assertEqual(mutiple_tuple((10**5, 10**5)), 10**10)

    def test_float_numbers(self):
        self.assertAlmostEqual(mutiple_tuple((1.5, 2.5)), 3.75)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            mutiple_tuple((1.5, 2))

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            mutiple_tuple(('a', 'b'))
