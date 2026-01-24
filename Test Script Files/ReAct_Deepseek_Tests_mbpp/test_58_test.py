import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))
        self.assertTrue(opposite_Signs(-1, -1))
        self.assertFalse(opposite_Signs(1, 1))

    def test_boundary_cases(self):
        self.assertTrue(opposite_Signs(0, -1))
        self.assertTrue(opposite_Signs(-1, 0))
        self.assertFalse(opposite_Signs(0, 0))
        self.assertFalse(opposite_Signs(0, 1))
        self.assertFalse(opposite_Signs(1, 0))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            opposite_Signs("a", 1)
        with self.assertRaises(TypeError):
            opposite_Signs(1, "b")
        with self.assertRaises(TypeError):
            opposite_Signs("a", "b")
