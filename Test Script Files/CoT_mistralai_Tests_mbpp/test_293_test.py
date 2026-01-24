import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), math.sqrt(25 + 16))
        self.assertAlmostEqual(otherside_rightangle(5, 12), math.sqrt(25 + 144))

    def test_zero_values(self):
        self.assertEqual(otherside_rightangle(0, 0), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(otherside_rightangle(-3, 4), math.sqrt(9 + 16))
        self.assertAlmostEqual(otherside_rightangle(-5, -12), math.sqrt(25 + 144))

    def test_one_zero_value(self):
        self.assertAlmostEqual(otherside_rightangle(0, 5), 5)
        self.assertAlmostEqual(otherside_rightangle(5, 0), 5)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, otherside_rightangle, 'a', 'b')
        self.assertRaises(TypeError, otherside_rightangle, 0, 'b')
        self.assertRaises(TypeError, otherside_rightangle, 'a', 0)
