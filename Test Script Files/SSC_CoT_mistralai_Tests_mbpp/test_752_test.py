import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(jacobsthal_num(1), 0)
        self.assertEqual(jacobsthal_num(2), 1)
        self.assertEqual(jacobsthal_num(3), 3)
        self.assertEqual(jacobsthal_num(4), 5)
        self.assertEqual(jacobsthal_num(5), 9)
        self.assertEqual(jacobsthal_num(6), 14)
        self.assertEqual(jacobsthal_num(7), 23)
        self.assertEqual(jacobsthal_num(8), 37)
        self.assertEqual(jacobsthal_num(9), 60)
        self.assertEqual(jacobsthal_num(10), 99)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(100), 3178)
        self.assertEqual(jacobsthal_num(-1), None)
        self.assertEqual(jacobsthal_num(None), None)
        self.assertEqual(jacobsthal_num("str"), None)
        self.assertEqual(jacobsthal_num(float("nan")), None)
        self.assertEqual(jacobsthal_num(complex(0, 1)), None)
