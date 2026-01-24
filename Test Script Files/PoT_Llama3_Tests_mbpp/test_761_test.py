import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(arc_length(10, 90), 31.416666666666668)

    def test_edge_case_a_360(self):
        self.assertIsNone(arc_length(10, 360))

    def test_edge_case_a_0(self):
        self.assertEqual(arc_length(10, 0), 0)

    def test_edge_case_d_0(self):
        self.assertEqual(arc_length(0, 90), 0)

    def test_invalid_input_d_negative(self):
        with self.assertRaises(TypeError):
            arc_length(-10, 90)

    def test_invalid_input_a_negative(self):
        with self.assertRaises(TypeError):
            arc_length(10, -90)

    def test_invalid_input_d_non_numeric(self):
        with self.assertRaises(TypeError):
            arc_length('ten', 90)

    def test_invalid_input_a_non_numeric(self):
        with self.assertRaises(TypeError):
            arc_length(10, 'ninety')
