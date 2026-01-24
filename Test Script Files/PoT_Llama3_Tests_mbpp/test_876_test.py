import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lcm(12, 15), 60)

    def test_edge_case_x_greater_y(self):
        self.assertEqual(lcm(15, 12), 60)

    def test_edge_case_y_greater_x(self):
        self.assertEqual(lcm(12, 15), 60)

    def test_edge_case_x_and_y_equal(self):
        self.assertEqual(lcm(12, 12), 12)

    def test_edge_case_x_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 15)

    def test_edge_case_y_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(15, 0)

    def test_edge_case_x_and_y_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 0)
