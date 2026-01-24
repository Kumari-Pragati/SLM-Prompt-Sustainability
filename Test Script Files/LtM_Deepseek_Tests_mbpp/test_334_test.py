import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(check_Validity(1, 2, 3))
        self.assertTrue(check_Validity(5, 12, 13))

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertFalse(check_Validity(0, 0, 0))
        self.assertFalse(check_Validity(1, 1, 2))
        self.assertFalse(check_Validity(1, 2, 3))
        self.assertFalse(check_Validity(1, 2, 4))
        self.assertFalse(check_Validity(1, 3, 4))
        self.assertFalse(check_Validity(2, 3, 4))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(check_Validity(1000000000, 1000000000, 1))
        self.assertFalse(check_Validity(1, 1000000000, 1000000000))
        self.assertFalse(check_Validity(1000000000, 1, 1000000000))
        self.assertFalse(check_Validity(1000000000, 1000000000, 1000000000))
