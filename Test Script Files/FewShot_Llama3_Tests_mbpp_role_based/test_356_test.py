import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_angle(60, 60), 60)

    def test_edge_case_a_zero(self):
        self.assertEqual(find_angle(0, 60), 120)

    def test_edge_case_b_zero(self):
        self.assertEqual(find_angle(60, 0), 120)

    def test_edge_case_a_and_b_zero(self):
        self.assertEqual(find_angle(0, 0), 180)

    def test_invalid_input_type_a(self):
        with self.assertRaises(TypeError):
            find_angle("a", 60)

    def test_invalid_input_type_b(self):
        with self.assertRaises(TypeError):
            find_angle(60, "b")
