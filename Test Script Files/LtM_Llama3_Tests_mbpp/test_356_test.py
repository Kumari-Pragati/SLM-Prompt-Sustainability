import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_simple_angles(self):
        self.assertEqual(find_angle(60, 60), 60)
        self.assertEqual(find_angle(30, 30), 120)
        self.assertEqual(find_angle(90, 90), 0)

    def test_edge_angles(self):
        self.assertEqual(find_angle(0, 0), 180)
        self.assertEqual(find_angle(180, 180), 0)
        self.assertEqual(find_angle(90, 0), 90)

    def test_invalid_angles(self):
        with self.assertRaises(TypeError):
            find_angle('a', 60)
        with self.assertRaises(TypeError):
            find_angle(60, 'b')
