import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(toggle_middle_bits(0), 1)
        self.assertEqual(toggle_middle_bits(2), 3)
        self.assertEqual(toggle_middle_bits(5), 7)
        self.assertEqual(toggle_middle_bits(10), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(toggle_middle_bits(1), 1)
        self.assertEqual(toggle_middle_bits(127), 126)
        self.assertEqual(toggle_middle_bits(128), 127)
        self.assertEqual(toggle_middle_bits(129), 128)
        self.assertEqual(toggle_middle_bits(2147483647), 2147483645)
        self.assertEqual(toggle_middle_bits(2147483648), 2147483647)

    def test_complex_inputs(self):
        self.assertEqual(toggle_middle_bits(123456789), 123456787)
        self.assertEqual(toggle_middle_bits(2147483647 * 2), 2147483645 * 2)
        self.assertEqual(toggle_middle_bits(2147483647 * 3), 2147483645 * 3)
