import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(closest_num(10), 9)
        self.assertEqual(closest_num(0), -1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(closest_num(-1), 0)
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(2147483647), 2147483646)
        self.assertEqual(closest_num(-2147483648), -2147483647)

    def test_invalid_input(self):
        self.assertRaises(TypeError, closest_num, "invalid_input")
        self.assertRaises(TypeError, closest_num, None)
