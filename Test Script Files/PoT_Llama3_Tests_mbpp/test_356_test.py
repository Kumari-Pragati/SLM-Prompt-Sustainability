import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_angle(60, 60), 60)

    def test_edge_case_a_zero(self):
        self.assertEqual(find_angle(0, 90), 90)

    def test_edge_case_b_zero(self):
        self.assertEqual(find_angle(90, 0), 90)

    def test_edge_case_a_and_b_zero(self):
        self.assertEqual(find_angle(0, 0), 180)

    def test_edge_case_a_and_b_max(self):
        self.assertEqual(find_angle(90, 90), 0)

    def test_edge_case_a_max_b_zero(self):
        self.assertEqual(find_angle(90, 0), 90)

    def test_edge_case_b_max_a_zero(self):
        self.assertEqual(find_angle(0, 90), 90)

    def test_edge_case_a_and_b_max(self):
        self.assertEqual(find_angle(90, 90), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_angle('a', 'b')

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            find_angle(180, 180)
