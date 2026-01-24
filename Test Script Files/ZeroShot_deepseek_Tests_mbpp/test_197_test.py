import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2**4, 3**5),))

    def test_negative_numbers(self):
        self.assertEqual(find_exponentio((-2, -3), (4, 5)), ((-2**4, -3**5),))

    def test_mixed_numbers(self):
        self.assertEqual(find_exponentio((2, -3), (4, 5)), ((2**4, -3**5),))

    def test_zero(self):
        self.assertEqual(find_exponentio((0, 0), (4, 5)), ((0**4, 0**5),))

    def test_large_numbers(self):
        self.assertEqual(find_exponentio((10, 10), (10, 10)), ((10**10, 10**10),))
