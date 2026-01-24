import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_angle(30, 60), 90)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(180, 0), 0)

    def test_edge_case(self):
        self.assertEqual(find_angle(0, 90), 90)
        self.assertEqual(find_angle(90, 0), 90)
        self.assertEqual(find_angle(180, 180), 0)
        self.assertEqual(find_angle(0, 0), 180)

    def test_boundary_case(self):
        self.assertEqual(find_angle(0, 359), 180)
        self.assertEqual(find_angle(359, 0), 180)
        self.assertEqual(find_angle(359, 359), 0)
