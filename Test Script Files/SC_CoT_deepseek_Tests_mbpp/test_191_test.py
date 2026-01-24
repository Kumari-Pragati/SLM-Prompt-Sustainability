import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber(""))
        self.assertFalse(check_monthnumber(" "))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("December"))

    def test_corner_cases(self):
        self.assertFalse(check_monthnumber("april"))
        self.assertFalse(check_monthnumber("JUNE"))
        self.assertFalse(check_monthnumber("sePTEMBER"))
        self.assertFalse(check_monthnumber("NOVEMBER!"))
        self.assertFalse(check_monthnumber("123"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_monthnumber(123)
        with self.assertRaises(TypeError):
            check_monthnumber(None)
