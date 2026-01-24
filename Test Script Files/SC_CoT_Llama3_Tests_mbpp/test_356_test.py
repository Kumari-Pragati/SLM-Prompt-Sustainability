import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_angle(60, 60), 60)

    def test_edge_cases(self):
        self.assertEqual(find_angle(0, 180), 60)
        self.assertEqual(find_angle(180, 0), 60)
        self.assertEqual(find_angle(90, 90), 0)

    def test_boundary_cases(self):
        self.assertEqual(find_angle(170, 10), 0)
        self.assertEqual(find_angle(10, 170), 0)

    def test_special_cases(self):
        self.assertEqual(find_angle(90, 0), 90)
        self.assertEqual(find_angle(0, 90), 90)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_angle('a', 60)
        with self.assertRaises(TypeError):
            find_angle(60, 'b')
