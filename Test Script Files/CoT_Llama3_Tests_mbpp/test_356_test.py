import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_angles(self):
        self.assertEqual(find_angle(60, 60), 60)
        self.assertEqual(find_angle(30, 90), 60)
        self.assertEqual(find_angle(90, 30), 60)
        self.assertEqual(find_angle(45, 45), 90)

    def test_edge_cases(self):
        self.assertEqual(find_angle(0, 180), 60)
        self.assertEqual(find_angle(180, 0), 60)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(0, 0), 180)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_angle('a', 60)
        with self.assertRaises(TypeError):
            find_angle(60, 'b')
        with self.assertRaises(TypeError):
            find_angle('a', 'b')
