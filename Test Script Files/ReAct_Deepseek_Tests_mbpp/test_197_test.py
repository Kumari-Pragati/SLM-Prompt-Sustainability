import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2**4, 3**5)))

    def test_zero_exponent(self):
        self.assertEqual(find_exponentio((2, 3), (0, 0)), ((1, 1)))

    def test_negative_base(self):
        self.assertEqual(find_exponentio((-2, -3), (4, 5)), ((-2**4, -3**5)))

    def test_zero_base(self):
        self.assertEqual(find_exponentio((0, 0), (4, 5)), ((0, 0)))

    def test_large_numbers(self):
        self.assertEqual(find_exponentio((10, 10), (10, 10)), ((10**10, 10**10)))

    def test_mixed_signs(self):
        self.assertEqual(find_exponentio((-2, 3), (4, -5)), ((-2**4, 3**-5)))

    def test_empty_tuples(self):
        self.assertEqual(find_exponentio((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(find_exponentio((2,), (3,)), ((2**3,)))
