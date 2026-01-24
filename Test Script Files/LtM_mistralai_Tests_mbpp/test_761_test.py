import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(arc_length(10, 90), 26.179938779914944)
        self.assertEqual(arc_length(2, 180), 10.47197551196597)
        self.assertEqual(arc_length(3, 270), 13.089968943659693)

    def test_edge_and_boundary(self):
        self.assertIsNone(arc_length(1, 361))
        self.assertIsNone(arc_length(0, 0))
        self.assertIsNone(arc_length(0, 360))
        self.assertIsNone(arc_length(1, 0))

    def test_complex(self):
        self.assertEqual(arc_length(0.5, 180), 1.5707963267948966)
        self.assertEqual(arc_length(10, 599), 1766.3493403746155)
        self.assertEqual(arc_length(10, 799), 2356.1944871792893)
