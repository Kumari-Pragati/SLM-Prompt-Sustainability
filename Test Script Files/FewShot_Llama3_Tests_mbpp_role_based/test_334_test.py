import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_invalid_input1(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input2(self):
        self.assertFalse(check_Validity(1, 3, 2))

    def test_invalid_input3(self):
        self.assertFalse(check_Validity(2, 1, 3))

    def test_invalid_input4(self):
        self.assertFalse(check_Validity(3, 2, 1))

    def test_invalid_input5(self):
        self.assertFalse(check_Validity(1, 1, 1))
