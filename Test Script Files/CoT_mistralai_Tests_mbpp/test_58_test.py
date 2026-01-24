import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):
    def test_opposite_signs_positive_positive(self):
        self.assertFalse(opposite_Signs(5, 5))

    def test_opposite_signs_negative_negative(self):
        self.assertFalse(opposite_Signs(-5, -5))

    def test_opposite_signs_positive_negative(self):
        self.assertTrue(opposite_Signs(5, -5))

    def test_opposite_signs_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_opposite_signs_edge_cases(self):
        self.assertTrue(opposite_Signs(sys.maxsize, -sys.maxsize))
        self.assertTrue(opposite_Signs(-sys.maxsize, sys.maxsize))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, opposite_Signs, "string", 5)
        self.assertRaises(TypeError, opposite_Signs, 5, "string")
