import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthnumNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_monthnum_number(2))

    def test_non_typical_case(self):
        self.assertFalse(check_monthnum_number(1))

    def test_boundary_conditions(self):
        self.assertTrue(check_monthnum_number(2))
        self.assertFalse(check_monthnum_number(3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_monthnum_number('2')
        with self.assertRaises(TypeError):
            check_monthnum_number(3.5)
        with self.assertRaises(TypeError):
            check_monthnum_number(None)
