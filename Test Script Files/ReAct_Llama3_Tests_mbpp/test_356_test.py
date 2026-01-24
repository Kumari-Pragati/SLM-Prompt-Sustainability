import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_angles(self):
        self.assertEqual(find_angle(60, 60), 60)

    def test_edge_case_angles(self):
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(0, 0), 180)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_angle('a', 'b')

    def test_negative_angles(self):
        self.assertEqual(find_angle(-30, 30), 120)

    def test_large_angles(self):
        self.assertEqual(find_angle(150, 150), 30)
