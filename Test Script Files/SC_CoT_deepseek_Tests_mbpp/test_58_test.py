import unittest

from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))

    def test_zero_case(self):
        self.assertFalse(opposite_Signs(0, 0))
        self.assertFalse(opposite_Signs(0, 1))
        self.assertFalse(opposite_Signs(-1, 0))

    def test_boundary_case(self):
        self.assertTrue(opposite_Signs(2**31, -(2**31)))
        self.assertTrue(opposite_Signs(-(2**31), 2**31))

    def test_negative_case(self):
        self.assertFalse(opposite_Signs(-1, -1))
        self.assertFalse(opposite_Signs(1, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            opposite_Signs("a", 1)
        with self.assertRaises(TypeError):
            opposite_Signs(1, "b")
        with self.assertRaises(TypeError):
            opposite_Signs("a", "b")
