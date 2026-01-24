import unittest
from499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(diameter_circle(3), 6)
        self.assertEqual(diameter_circle(5), 10)

    def test_zero(self):
        self.assertEqual(diameter_circle(0), 0)

    def test_negative_number(self):
        self.assertEqual(diameter_circle(-1), 2)

    def test_float(self):
        self.assertAlmostEqual(diameter_circle(2.5), 5)

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            diameter_circle('str')
