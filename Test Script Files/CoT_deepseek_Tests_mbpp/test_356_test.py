import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(find_angle(30, 60), 90)

    def test_edge_case_with_zero(self):
        self.assertAlmostEqual(find_angle(0, 0), 180)

    def test_edge_case_with_180(self):
        self.assertAlmostEqual(find_angle(180, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_angle("30", 60)
