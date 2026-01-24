import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(are_Rotations('ABCD', 'CDAB'))
        self.assertTrue(are_Rotations('XYZ', 'ZXY'))

    def test_edge_cases(self):
        self.assertFalse(are_Rotations('A', 'B'))
        self.assertFalse(are_Rotations('', 'A'))
        self.assertFalse(are_Rotations('A', ''))
        self.assertFalse(are_Rotations('', ''))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            are_Rotations(123, 'ABCD')
        with self.assertRaises(TypeError):
            are_Rotations('ABCD', 123)
        with self.assertRaises(TypeError):
            are_Rotations(123, 456)
