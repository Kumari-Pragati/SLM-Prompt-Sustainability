import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_monthnumber(""))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("April_incorrect_case"))
        self.assertFalse(check_monthnumber("june"))
        self.assertFalse(check_monthnumber("september_incorrect_case"))
        self.assertFalse(check_monthnumber("november_incorrect_case"))

    def test_more_complex_scenarios(self):
        self.assertFalse(check_monthnumber(""))
        self.assertFalse(check_monthnumber("April "))
        self.assertFalse(check_monthnumber("April, May"))
        self.assertFalse(check_monthnumber("April-May"))
        self.assertFalse(check_monthnumber("April_2022"))
        self.assertFalse(check_monthnumber("April_2022_12"))
