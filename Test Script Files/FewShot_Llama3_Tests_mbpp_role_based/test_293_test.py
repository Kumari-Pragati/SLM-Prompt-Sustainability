import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    def test_typical_use_case(self):
        w = 3
        h = 4
        expected_result = math.sqrt(3**2 + 4**2)
        self.assertAlmostEqual(otherside_rightangle(w, h), expected_result)

    def test_zero_width(self):
        w = 0
        h = 5
        expected_result = 5
        self.assertEqual(otherside_rightangle(w, h), expected_result)

    def test_zero_height(self):
        w = 6
        h = 0
        expected_result = 6
        self.assertEqual(otherside_rightangle(w, h), expected_result)

    def test_negative_width(self):
        w = -3
        h = 4
        expected_result = math.sqrt((-3)**2 + 4**2)
        self.assertAlmostEqual(otherside_rightangle(w, h), expected_result)

    def test_negative_height(self):
        w = 3
        h = -4
        expected_result = math.sqrt(3**2 + (-4)**2)
        self.assertAlmostEqual(otherside_rightangle(w, h), expected_result)

    def test_zero_width_and_height(self):
        w = 0
        h = 0
        expected_result = 0
        self.assertEqual(otherside_rightangle(w, h), expected_result)
