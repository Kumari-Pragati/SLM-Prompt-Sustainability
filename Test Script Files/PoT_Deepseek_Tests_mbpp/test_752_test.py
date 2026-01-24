import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(5), 21)
        self.assertEqual(jacobsthal_num(10), 1094)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_num(-1), 0)
        self.assertEqual(jacobsthal_num(20), 1048575)

    def test_boundary_cases(self):
        self.assertEqual(jacobsthal_num(21), 2097151)
        self.assertEqual(jacobsthal_num(22), 4194303)
