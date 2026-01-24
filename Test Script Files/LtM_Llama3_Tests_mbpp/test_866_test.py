import unittest
from mbpp_866_code import check_monthnumb

class TestCheckMonthnumb(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_monthnumb("January"))
        self.assertTrue(check_monthnumb("March"))
        self.assertTrue(check_monthnumb("May"))
        self.assertTrue(check_monthnumb("July"))
        self.assertTrue(check_monthnumb("August"))
        self.assertTrue(check_monthnumb("October"))
        self.assertTrue(check_monthnumb("December"))

    def test_invalid_inputs(self):
        self.assertFalse(check_monthnumb("February"))
        self.assertFalse(check_monthnumb("April"))
        self.assertFalse(check_monthnumb("June"))
        self.assertFalse(check_monthnumb("September"))
        self.assertFalse(check_monthnumb("November"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumb("Jan"))
        self.assertFalse(check_monthnumb("MARCH"))
        self.assertFalse(check_monthnumb("august"))
