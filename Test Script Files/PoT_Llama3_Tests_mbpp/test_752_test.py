import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(jacobsthal_num(3), 2)

    def test_edge_case(self):
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 1)

    def test_boundary_case(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(4), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            jacobsthal_num('a')
