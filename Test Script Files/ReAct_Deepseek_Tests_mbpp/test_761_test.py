import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(arc_length(10, 90), 22/7 * 10 * 0.25, places=2)

    def test_typical_case_with_larger_angle(self):
        self.assertAlmostEqual(arc_length(10, 180), 22/7 * 10, places=2)

    def test_boundary_case_with_360_degrees(self):
        self.assertIsNone(arc_length(10, 360))

    def test_boundary_case_with_0_degrees(self):
        self.assertEqual(arc_length(10, 0), 0)

    def test_negative_angle(self):
        self.assertIsNone(arc_length(10, -10))

    def test_large_diameter(self):
        self.assertAlmostEqual(arc_length(10000, 90), 22/7 * 10000 * 0.25, places=2)

    def test_large_angle(self):
        self.assertAlmostEqual(arc_length(10, 3600), 22/7 * 10 * 10, places=2)

    def test_zero_diameter(self):
        self.assertIsNone(arc_length(0, 90))

    def test_none_diameter(self):
        self.assertIsNone(arc_length(None, 90))

    def test_string_diameter(self):
        self.assertIsNone(arc_length("10", 90))

    def test_list_diameter(self):
        self.assertIsNone(arc_length([10], 90))
