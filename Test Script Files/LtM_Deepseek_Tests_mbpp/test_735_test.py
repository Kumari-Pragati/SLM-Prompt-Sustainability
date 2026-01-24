import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(toggle_middle_bits(10), 14)
        self.assertEqual(toggle_middle_bits(15), 15)
        self.assertEqual(toggle_middle_bits(0), 1)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(toggle_middle_bits(1), 1)
        self.assertEqual(toggle_middle_bits(2**31 - 1), 2**31 - 1)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(toggle_middle_bits(2**31), 2**31)
        self.assertEqual(toggle_middle_bits(2**32 - 1), 2**32 - 1)
