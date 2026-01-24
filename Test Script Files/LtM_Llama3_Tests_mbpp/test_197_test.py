import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_exponentio((1, 2), (3, 4)), ((1**2, 1**3), (2**2, 2**3)))

    def test_empty_inputs(self):
        with self.assertRaises(TypeError):
            find_exponentio([], [])

    def test_single_element_tuples(self):
        self.assertEqual(find_exponentio((1,), (2,)), ((1**2,),))

    def test_zero_exponent(self):
        self.assertEqual(find_exponentio((1, 2), (0, 1)), ((1**0, 1**1),))

    def test_negative_exponent(self):
        self.assertEqual(find_exponentio((1, 2), (-1, -2)), ((1**-1, 1**-2),))

    def test_large_exponents(self):
        self.assertEqual(find_exponentio((1, 2), (100, 200)), ((1**100, 1**200),))

    def test_large_values(self):
        self.assertEqual(find_exponentio((1000000, 2000000), (3, 4)), ((1000000**3, 2000000**3),))
