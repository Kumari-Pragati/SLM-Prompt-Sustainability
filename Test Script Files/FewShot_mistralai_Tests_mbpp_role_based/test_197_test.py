import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2**4, 3**5)))
        self.assertEqual(find_exponentio((1, 2), (3, 4)), ((1**3, 2**4)))

    def test_zero_and_one(self):
        self.assertEqual(find_exponentio((0, 1), (0, 1)), ((0, 1)))
        self.assertEqual(find_exponentio((1, 0), (0, 1)), ((1, 0)) )

    def test_negative_numbers(self):
        self.assertEqual(find_exponentio((-2, -3), (-4, -5)), ((-2**-4, -3**-5)))
        self.assertEqual(find_exponentio((-1, -2), (-3, -4)), ((-1**-3, -2**-4)))

    def test_mixed_numbers(self):
        self.assertEqual(find_exponentio((2, -3, 0), (4, -5, 1)), ((2**4, -3**-5, 0**1)))
        self.assertEqual(find_exponentio((-2, 3, 0), (-4, -5, 1)), ((-2**-4, 3**-5, 0**1)))
