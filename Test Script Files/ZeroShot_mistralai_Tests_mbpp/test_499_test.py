import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_diameter_circle(self):
        self.assertEqual(diameter_circle(1), 2)
        self.assertEqual(diameter_circle(2.5), 5)
        self.assertAlmostEqual(diameter_circle(3.14), 6.28)
        self.assertRaises(TypeError, diameter_circle, 'not_a_number')
