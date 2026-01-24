import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_angle(30, 60), 90)

    def test_boundary_conditions(self):
        self.assertEqual(find_angle(0, 0), 180)
        self.assertEqual(find_angle(90, 0), 90)
        self.assertEqual(find_angle(0, 90), 90)
        self.assertEqual(find_angle(90, 90), 0)

    def test_edge_conditions(self):
        self.assertEqual(find_angle(180, 0), 0)
        self.assertEqual(find_angle(0, 180), 0)
        self.assertEqual(find_angle(180, 180), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_angle('30', 60)
        with self.assertRaises(TypeError):
            find_angle(30, '60')
        with self.assertRaises(ValueError):
            find_angle(200, 60)
        with self.assertRaises(ValueError):
            find_angle(30, 200)
