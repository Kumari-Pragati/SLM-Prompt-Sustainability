import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)

    def test_zero_input(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(otherside_rightangle(3, 0), 3.0)

    def test_edge_case_zero_reverse(self):
        self.assertAlmostEqual(otherside_rightangle(0, 3), 3.0)

    def test_edge_case_zero_both(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            otherside_rightangle("hello", 4)

    def test_invalid_input_type_reverse(self):
        with self.assertRaises(TypeError):
            otherside_rightangle(4, "hello")

    def test_invalid_input_type_both(self):
        with self.assertRaises(TypeError):
            otherside_rightangle("hello", "world")
