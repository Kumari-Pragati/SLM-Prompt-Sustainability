import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    # Test for simple / typical inputs
    def test_simple_inputs(self):
        self.assertTrue(are_Rotations('ABCD', 'CDAB'))
        self.assertTrue(are_Rotations('1234', '4123'))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertTrue(are_Rotations('', ''))
        self.assertFalse(are_Rotations('A', 'B'))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertTrue(are_Rotations('waterbottle', 'erbottlewat'))
        self.assertFalse(are_Rotations('ABCD', 'DCAB'))
        self.assertFalse(are_Rotations('ABCD', 'ABDC'))
