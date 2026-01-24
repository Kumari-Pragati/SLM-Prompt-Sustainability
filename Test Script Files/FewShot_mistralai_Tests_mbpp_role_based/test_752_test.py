import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(3), 4)
        self.assertEqual(jacobsthal_num(4), 7)
        self.assertEqual(jacobsthal_num(5), 11)
        self.assertEqual(jacobsthal_num(6), 15)
        self.assertEqual(jacobsthal_num(7), 22)
        self.assertEqual(jacobsthal_num(8), 29)
        self.assertEqual(jacobsthal_num(9), 37)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(jacobsthal_num(-1), None)
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2**31 - 1), 2147483646)
        self.assertEqual(jacobsthal_num(2**31), None)
