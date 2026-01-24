import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_angle(30, 60), 90)
        self.assertEqual(find_angle(45, 45), 90)

    def test_boundary_conditions(self):
        self.assertEqual(find_angle(0, 0), 180)
        self.assertEqual(find_angle(0, 180), 0)
        self.assertEqual(find_angle(180, 0), 0)
        self.assertEqual(find_angle(90, 90), 0)

    def test_edge_cases(self):
        self.assertEqual(find_angle(180, 1), 1)
        self.assertEqual(find_angle(1, 179), 1)
        self.assertEqual(find_angle(91, 89), 1)
        self.assertEqual(find_angle(89, 91), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_angle("30", 60)
        with self.assertRaises(TypeError):
            find_angle(30, "60")
        with self.assertRaises(ValueError):
            find_angle(200, 60)
        with self.assertRaises(ValueError):
            find_angle(30, 200)
