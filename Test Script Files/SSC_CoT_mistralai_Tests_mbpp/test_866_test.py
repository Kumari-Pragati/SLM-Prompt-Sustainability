import unittest
from mbpp_866_code import check_monthnumb

class TestCheckMonthnumb(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(check_monthnumb("January"))
        self.assertTrue(check_monthnumb("March"))
        self.assertTrue(check_monthnumb("May"))
        self.assertTrue(check_monthnumb("July"))
        self.assertTrue(check_monthnumb("August"))
        self.assertTrue(check_monthnumb("October"))
        self.assertTrue(check_monthnumb("December"))

    def test_edge_input(self):
        self.assertFalse(check_monthnumb("January31"))
        self.assertTrue(check_monthnumb("February28"))
        self.assertFalse(check_monthnumb("February29"))
        self.assertTrue(check_monthnumb("April"))
        self.assertTrue(check_monthnumb("June"))
        self.assertTrue(check_monthnumb("November"))
        self.assertTrue(check_monthnumb("November30"))
        self.assertFalse(check_monthnumb("November31"))

    def test_invalid_input(self):
        self.assertFalse(check_monthnumb(""))
        self.assertFalse(check_monthnumb("abc"))
        self.assertFalse(check_monthnumb(None))
        self.assertFalse(check_monthnumb(123))
