import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))
        self.assertTrue(opposite_Signs(-1, -1))
        self.assertFalse(opposite_Signs(0, 0))
        self.assertFalse(opposite_Signs(1, 1))

    def test_edge_cases(self):
        self.assertTrue(opposite_Signs(float('-inf'), float('inf')))
        self.assertTrue(opposite_Signs(float('inf'), float('-inf')))
        self.assertFalse(opposite_Signs(float('-inf'), float('-inf')))
        self.assertFalse(opposite_Signs(float('inf'), float('inf')))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            opposite_Signs("a", 1)
        with self.assertRaises(TypeError):
            opposite_Signs(1, "a")
        with self.assertRaises(TypeError):
            opposite_Signs("a", "b")
