import unittest
from mbpp_252_code import convert
import cmath

class TestConvert(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(convert(cmath.rect(1, 1)), (1, 1))

    def test_boundary_condition(self):
        self.assertEqual(convert(cmath.rect(0, 0)), (0, 0))

    def test_edge_condition(self):
        self.assertEqual(convert(cmath.rect(1, 0)), (1, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            convert("invalid input")
