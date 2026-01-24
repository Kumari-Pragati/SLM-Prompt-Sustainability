import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2**4, 3**5)))
        self.assertEqual(find_exponentio((10, 2), (3, 4)), ((10**3, 2**4)))
        self.assertEqual(find_exponentio((1, 2), (10, 10)), ((1**10, 2**10)))

    def test_zero_as_base(self):
        self.assertRaises(ValueError, find_exponentio, (2, 0))

    def test_negative_numbers(self):
        self.assertEqual(find_exponentio((-2, 3), (4, 5)), ((-2**4, 3**5)))
        self.assertEqual(find_exponentio((-10, -2), (3, 4)), ((-10**3, -2**4)))
        self.assertEqual(find_exponentio((-1, -2), (-10, -10)), ((-1**10, -2**10)))

    def test_floats(self):
        self.assertAlmostEqual(find_exponentio((2.5, 3), (4, 5)), ((2.5**4, 3**5)))
        self.assertAlmostEqual(find_exponentio((10.5, 2), (3, 4)), ((10.5**3, 2**4)))
        self.assertAlmostEqual(find_exponentio((1.5, 2), (10, 10)), ((1.5**10, 2**10)))

    def test_mixed_types(self):
        self.assertRaises(TypeError, find_exponentio, (2, '3'))
        self.assertRaises(TypeError, find_exponentio, ('2', 3))
