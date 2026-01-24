import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthnumber(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("July"))
        self.assertFalse(check_monthnumber("August"))
        self.assertFalse(check_monthnumber("October"))
        self.assertFalse(check_monthnumber("December"))

    def test_invalid_inputs(self):
        self.assertFalse(check_monthnumber("Invalid"))
        self.assertFalse(check_monthnumber(""))
