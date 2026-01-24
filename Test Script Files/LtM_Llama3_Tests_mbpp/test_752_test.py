import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 4)
        self.assertEqual(jacobsthal_num(4), 6)
        self.assertEqual(jacobsthal_num(5), 10)

    def test_edge(self):
        self.assertEqual(jacobsthal_num(-1), 0)
        self.assertEqual(jacobsthal_num(-2), 0)
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)

    def test_large(self):
        self.assertEqual(jacobsthal_num(10), 143)
        self.assertEqual(jacobsthal_num(20), 2867)
        self.assertEqual(jacobsthal_num(30), 103886)
