import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))
        self.assertFalse(opposite_Signs(1, 1))
        self.assertFalse(opposite_Signs(-1, -1))

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertTrue(opposite_Signs(0, -1))
        self.assertTrue(opposite_Signs(-1, 0))
        self.assertFalse(opposite_Signs(0, 0))
        self.assertFalse(opposite_Signs(0, 1))
        self.assertFalse(opposite_Signs(1, 0))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertTrue(opposite_Signs(-1000000, 1000000))
        self.assertTrue(opposite_Signs(1000000, -1000000))
        self.assertFalse(opposite_Signs(1000000, 1000000))
        self.assertFalse(opposite_Signs(-1000000, -1000000))
