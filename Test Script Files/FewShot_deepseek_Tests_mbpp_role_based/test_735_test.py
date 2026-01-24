import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(toggle_middle_bits(10), 6)

    def test_boundary_conditions(self):
        self.assertEqual(toggle_middle_bits(0), 0)
        self.assertEqual(toggle_middle_bits(1), 1)

    def test_edge_cases(self):
        self.assertEqual(toggle_middle_bits(255), 254)
        self.assertEqual(toggle_middle_bits(256), 1)
        self.assertEqual(toggle_middle_bits(511), 510)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits('a')
        with self.assertRaises(TypeError):
            toggle_middle_bits(None)
