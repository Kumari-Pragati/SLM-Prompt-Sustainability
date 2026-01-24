import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 5)

    def test_complex_cases(self):
        self.assertEqual(jacobsthal_num(4), 10)
        self.assertEqual(jacobsthal_num(5), 21)

    def test_large_numbers(self):
        self.assertEqual(jacobsthal_num(10), 16449)
        self.assertEqual(jacobsthal_num(20), 58084378297)
