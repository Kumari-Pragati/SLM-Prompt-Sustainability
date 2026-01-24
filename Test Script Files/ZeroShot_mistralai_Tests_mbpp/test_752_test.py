import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_jacobsthal_num_with_zero(self):
        self.assertEqual(jacobsthal_num(0), 0)

    def test_jacobsthal_num_with_one(self):
        self.assertEqual(jacobsthal_num(1), 1)

    def test_jacobsthal_num_with_small_numbers(self):
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(3), 5)
        self.assertEqual(jacobsthal_num(4), 9)
        self.assertEqual(jacobsthal_num(5), 14)

    def test_jacobsthal_num_with_large_numbers(self):
        self.assertEqual(jacobsthal_num(100), 1994983642)
        self.assertEqual(jacobsthal_num(1000), 4999999987)
