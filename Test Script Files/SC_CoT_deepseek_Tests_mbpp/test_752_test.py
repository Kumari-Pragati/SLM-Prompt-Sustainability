import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(5), 21)
        self.assertEqual(jacobsthal_num(10), 1440)

    def test_boundary_conditions(self):
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(3), 7)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_num(20), 1048575)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            jacobsthal_num('a')
        with self.assertRaises(ValueError):
            jacobsthal_num(-1)
