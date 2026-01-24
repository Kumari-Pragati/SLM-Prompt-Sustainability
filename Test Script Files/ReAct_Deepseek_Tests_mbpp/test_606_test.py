import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(radian_degree(90), math.pi/2)

    def test_zero_degree(self):
        self.assertAlmostEqual(radian_degree(0), 0)

    def test_negative_degree(self):
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2)

    def test_large_degree(self):
        self.assertAlmostEqual(radian_degree(360), math.pi*2)

    def test_large_negative_degree(self):
        self.assertAlmostEqual(radian_degree(-360), -math.pi*2)

    def test_non_integer_degree(self):
        self.assertAlmostEqual(radian_degree(45.5), math.pi/4*2)

    def test_large_non_integer_degree(self):
        self.assertAlmostEqual(radian_degree(360.5), math.pi*2 + math.pi/2)

    def test_large_negative_non_integer_degree(self):
        self.assertAlmostEqual(radian_degree(-360.5), -math.pi*2 - math.pi/2)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            radian_degree('abc')
