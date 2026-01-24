import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(arc_length(10, 90), 28.274333882308138)
        self.assertEqual(arc_length(2.5, 180), 15.707963267948966)
        self.assertEqual(arc_length(0.1, 360), 628.3185307179586)

    def test_edge_case(self):
        self.assertIsNone(arc_length(1, 361))
        self.assertIsNone(arc_length(0, -10))
        self.assertIsNone(arc_length(0, 0))

    def test_corner_case(self):
        self.assertEqual(arc_length(0, 180), 5.7105957417726805)
        self.assertEqual(arc_length(1, 720), 2006.535861957268)
