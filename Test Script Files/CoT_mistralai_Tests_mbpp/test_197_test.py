import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTupleEqual(find_exponentio((2, 3, 4), (7, 2, 5)), ((2**7, 3**2, 4**5)))
        self.assertTupleEqual(find_exponentio((10, 5, 2), (3, 2, 4)), ((10**3, 5**2, 2**4)))

    def test_zero_and_negative_numbers(self):
        self.assertTupleEqual(find_exponentio((-2, 0, 3), (2, 0, -3)), ((-2**2, 0**0, 3**-3)))
        self.assertTupleEqual(find_exponentio((0, -2, 3), (2, 0, -3)), ((0**2, -2**0, 3**-3)))

    def test_floats(self):
        self.assertAlmostEqual(find_exponentio((2.5, 3, 4), (7, 2, 5)), ((2.5**7, 3**2, 4**5)))
        self.assertAlmostEqual(find_exponentio((10.0, 5.5, 2.2), (3, 2, 4)), ((10.0**3, 5.5**2, 2.2**4)))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            find_exponentio((2, '3', 4), (7, 2, 5))
        with self.assertRaises(TypeError):
            find_exponentio((2, 3, '4'), (7, 2, 5))
