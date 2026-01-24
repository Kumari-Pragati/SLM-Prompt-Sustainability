import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(jacobsthal_num(0), 0)

    def test_one(self):
        self.assertEqual(jacobsthal_num(1), 1)

    def test_small(self):
        self.assertEqual(jacobsthal_num(5), 2)

    def test_large(self):
        self.assertEqual(jacobsthal_num(10), 34)

    def test_negative(self):
        with self.assertRaises(ValueError):
            jacobsthal_num(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            jacobsthal_num(3.5)
