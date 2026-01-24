import unittest
from mbpp_518_code import sqrt

def sqrt_root(num):
    return math.pow(num, 0.5)

class TestSqrtRoot(unittest.TestCase):

    def test_sqrt_root_positive_numbers(self):
        for num, expected in [(1, 1), (4, 2), (9, 3), (25, 5)]:
            with self.subTest(num=num):
                self.assertAlmostEqual(sqrt_root(num), expected)

    def test_sqrt_root_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0)

    def test_sqrt_root_negative_numbers(self):
        for num, expected in [(-1, -1), (-4, -2), (-9, -3), (-25, -5)]:
            with self.subTest(num=num):
                self.assertAlmostEqual(sqrt_root(num), expected)

    def test_sqrt_root_non_number(self):
        self.assertRaises(TypeError, sqrt_root, 'not a number')
