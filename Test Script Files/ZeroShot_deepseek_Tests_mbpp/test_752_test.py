import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_jacobsthal_num(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 5)
        self.assertEqual(jacobsthal_num(4), 10)
        self.assertEqual(jacobsthal_num(5), 21)
        self.assertEqual(jacobsthal_num(6), 42)
        self.assertEqual(jacobsthal_num(7), 85)
        self.assertEqual(jacobsthal_num(8), 170)
        self.assertEqual(jacobsthal_num(9), 341)
        self.assertEqual(jacobsthal_num(10), 682)
