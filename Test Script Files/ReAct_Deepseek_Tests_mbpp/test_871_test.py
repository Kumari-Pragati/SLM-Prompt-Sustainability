import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(are_Rotations('ABCD', 'CDAB'))
        self.assertTrue(are_Rotations('1234', '4123'))
        self.assertTrue(are_Rotations('hello', 'lohel'))

    def test_empty_strings(self):
        self.assertTrue(are_Rotations('', ''))

    def test_same_string(self):
        self.assertTrue(are_Rotations('ABCD', 'ABCD'))

    def test_different_lengths(self):
        self.assertFalse(are_Rotations('ABCD', 'ABCDAB'))
        self.assertFalse(are_Rotations('123', '1234'))

    def test_case_sensitivity(self):
        self.assertFalse(are_Rotations('AbCd', 'dAbC'))

    def test_special_characters(self):
        self.assertTrue(are_Rotations('!@#$', '$!@#'))
        self.assertFalse(are_Rotations('!@#$', '$!@'))
