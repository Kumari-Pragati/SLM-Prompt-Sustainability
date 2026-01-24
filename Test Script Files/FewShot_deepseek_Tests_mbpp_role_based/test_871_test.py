import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(are_Rotations('ABCD', 'CDAB'))

    def test_edge_case(self):
        self.assertTrue(are_Rotations('A', 'A'))

    def test_boundary_case(self):
        self.assertFalse(are_Rotations('ABCD', 'DCAB'))

    def test_different_lengths(self):
        self.assertFalse(are_Rotations('ABCD', 'ABC'))

    def test_empty_strings(self):
        self.assertTrue(are_Rotations('', ''))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            are_Rotations(123, 'ABCD')
