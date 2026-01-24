import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_jacobsthal_num_zero(self):
        self.assertEqual(jacobsthal_num(0), 0)

    def test_jacobsthal_num_one(self):
        self.assertEqual(jacobsthal_num(1), 1)

    def test_jacobsthal_num_two(self):
        self.assertEqual(jacobsthal_num(2), 1)

    def test_jacobsthal_num_three(self):
        self.assertEqual(jacobsthal_num(3), 2)

    def test_jacobsthal_num_four(self):
        self.assertEqual(jacobsthal_num(4), 3)

    def test_jacobsthal_num_five(self):
        self.assertEqual(jacobsthal_num(5), 5)

    def test_jacobsthal_num_negative(self):
        with self.assertRaises(ValueError):
            jacobsthal_num(-1)

    def test_jacobsthal_num_non_integer(self):
        with self.assertRaises(TypeError):
            jacobsthal_num(3.5)
