import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(divisor(10), 2)

    def test_edge_condition(self):
        self.assertEqual(divisor(1), 1)

    def test_boundary_condition(self):
        self.assertEqual(divisor(0), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            divisor('a')
