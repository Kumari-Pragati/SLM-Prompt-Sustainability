import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_are_rotations(self):
        self.assertTrue(are_Rotations('ABCD', 'CDAB'))
        self.assertTrue(are_Rotations('ACBA', 'BACA'))
        self.assertFalse(are_Rotations('ABCD', 'ACBD'))
        self.assertFalse(are_Rotations('AABCD', 'CDABA'))
        self.assertFalse(are_Rotations('ABCD', 'ABCDX'))
        self.assertFalse(are_Rotations('ABCD', 'ABCE'))
