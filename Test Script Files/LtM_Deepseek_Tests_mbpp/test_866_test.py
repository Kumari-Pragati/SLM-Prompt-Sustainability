import unittest
from mbpp_866_code import check_monthnumb

class TestCheckMonthnumb(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(check_monthnumb("January"))
        self.assertTrue(check_monthnumb("March"))
        self.assertTrue(check_monthnumb("May"))
        self.assertTrue(check_monthnumb("July"))
        self.assertTrue(check_monthnumb("August"))
        self.assertTrue(check_monthnumb("October"))
        self.assertTrue(check_monthnumb("December"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumb(""))
        self.assertFalse(check_monthnumb("InvalidMonth"))
        self.assertFalse(check_monthnumb("J"))
        self.assertFalse(check_monthnumb("December "))
        self.assertFalse(check_monthnumb("december"))

    def test_complex_cases(self):
        self.assertTrue(check_monthnumb("DecEmber"))
        self.assertFalse(check_monthnumb("DecEmber "))
        self.assertFalse(check_monthnumb("DecEmber "))
        self.assertFalse(check_monthnumb("DecEmber"))
