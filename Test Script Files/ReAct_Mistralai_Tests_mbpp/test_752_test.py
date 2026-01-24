import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(5), 24)
        self.assertEqual(jacobsthal_num(10), 109)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_num(100), 4759)
        self.assertEqual(jacobsthal_num(1000), 2377609)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            jacobsthal_num(-1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            jacobsthal_num(0)
