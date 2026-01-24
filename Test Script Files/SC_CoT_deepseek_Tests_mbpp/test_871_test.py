import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertTrue(are_Rotations('ABCD', 'CDAB'))
        self.assertTrue(are_Rotations('1234', '4123'))
        self.assertTrue(are_Rotations('waterbottle', 'erbottlewat'))

    def test_edge_cases(self):
        self.assertTrue(are_Rotations('', ''))
        self.assertFalse(are_Rotations('A', 'B'))

    def test_corner_cases(self):
        self.assertFalse(are_Rotations('ABC', 'ACB'))
        self.assertFalse(are_Rotations('ABCD', 'DCBA'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            are_Rotations(1234, 'ABCD')
        with self.assertRaises(TypeError):
            are_Rotations('ABCD', 1234)
