import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(3), 6)
        self.assertEqual(jacobsthal_num(4), 11)
        self.assertEqual(jacobsthal_num(5), 20)
        self.assertEqual(jacobsthal_num(6), 35)
        self.assertEqual(jacobsthal_num(7), 56)
        self.assertEqual(jacobsthal_num(8), 89)
        self.assertEqual(jacobsthal_num(9), 144)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(jacobsthal_num(-1), None)
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(20), 1061)
        self.assertEqual(jacobsthal_num(30), 3465)
        self.assertEqual(jacobsthal_num(40), 7752)
        self.assertEqual(jacobsthal_num(50), 15005)
        self.assertEqual(jacobsthal_num(100), 67090)
