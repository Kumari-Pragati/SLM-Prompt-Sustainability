import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(3), 7)
        self.assertEqual(jacobsthal_num(4), 15)
        self.assertEqual(jacobsthal_num(5), 31)

    def test_edge_and_boundary(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(6), 63)
        self.assertEqual(jacobsthal_num(7), 149)
        self.assertEqual(jacobsthal_num(8), 331)
        self.assertEqual(jacobsthal_num(9), 701)

    def test_complex(self):
        self.assertEqual(jacobsthal_num(10), 1441)
        self.assertEqual(jacobsthal_num(20), 60791)
        self.assertEqual(jacobsthal_num(30), 2154781)
        self.assertEqual(jacobsthal_num(40), 77203641)
        self.assertEqual(jacobsthal_num(50), 2812976031)
