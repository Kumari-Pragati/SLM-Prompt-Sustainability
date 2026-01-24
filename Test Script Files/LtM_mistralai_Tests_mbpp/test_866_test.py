import unittest
from mbpp_866_code import check_monthnumb

class TestCheckMonthnumb(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(check_monthnumb("January"))
        self.assertTrue(check_monthnumb("March"))
        self.assertTrue(check_monthnumb("May"))
        self.assertTrue(check_monthnumb("July"))
        self.assertTrue(check_monthnumb("August"))
        self.assertTrue(check_monthnumb("October"))
        self.assertTrue(check_monthnumb("December"))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_monthnumb("February"))
        self.assertFalse(check_monthnumb("April"))
        self.assertFalse(check_monthnumb("June"))
        self.assertFalse(check_monthnumb("November"))
        self.assertFalse(check_monthnumb("September"))
        self.assertFalse(check_monthnumb(""))
        self.assertFalse(check_monthnumb("January "))
        self.assertFalse(check_monthnumb("January123"))

    def test_more_complex_cases(self):
        self.assertFalse(check_monthnumb("January-2022"))
        self.assertFalse(check_monthnumb("January, 2022"))
        self.assertFalse(check_monthnumb("Jan-2022"))
        self.assertFalse(check_monthnumb("January2022"))
        self.assertFalse(check_monthnumb("January 2022"))
        self.assertFalse(check_monthnumb("January 2022Z"))
        self.assertFalse(check_monthnumb("January 2022T"))
