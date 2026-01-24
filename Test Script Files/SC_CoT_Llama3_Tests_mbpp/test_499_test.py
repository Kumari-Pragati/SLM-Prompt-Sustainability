import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(diameter_circle(5), 10)

    def test_edge_case_zero(self):
        self.assertEqual(diameter_circle(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            diameter_circle(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            diameter_circle('five')

    def test_edge_case_large_input(self):
        self.assertEqual(diameter_circle(1000), 2000)

    def test_edge_case_max_input(self):
        self.assertEqual(diameter_circle(2**31-1), 2**31-1*2)
