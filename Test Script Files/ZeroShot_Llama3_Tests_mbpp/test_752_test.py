import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_jacobsthal_num(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 4)
        self.assertEqual(jacobsthal_num(4), 6)
        self.assertEqual(jacobsthal_num(5), 10)
        self.assertEqual(jacobsthal_num(6), 16)
        self.assertEqual(jacobsthal_num(7), 26)
        self.assertEqual(jacobsthal_num(8), 42)
        self.assertEqual(jacobsthal_num(9), 68)

    def test_jacobsthal_num_edge_cases(self):
        self.assertRaises(ValueError, jacobsthal_num, -1)
        self.assertRaises(ValueError, jacobsthal_num, 0.5)
