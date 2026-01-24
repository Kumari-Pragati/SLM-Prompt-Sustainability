import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(convert(1+1j), (1.4142135623730951, 0.7853981633974483))

    def test_boundary_conditions(self):
        self.assertEqual(convert(0), (0, 0))
        self.assertEqual(convert(1), (1, 0))
        self.assertEqual(convert(-1), (1, 3.141592653589793))

    def test_edge_conditions(self):
        self.assertEqual(convert(1+0j), (1, 0))
        self.assertEqual(convert(-1+0j), (1, 3.141592653589793))
        self.assertEqual(convert(0+1j), (1.4142135623730951, 0.7853981633974483))
        self.assertEqual(convert(0-1j), (1.4142135623730951, -0.7853981633974483))

    def test_complex_scenarios(self):
        self.assertEqual(convert(1+1j), (1.4142135623730951, 0.7853981633974483))
        self.assertEqual(convert(-1-1j), (1.4142135623730951, 2.356194490192345))
