import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthnumber(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_case(self):
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("July"))
        self.assertFalse(check_monthnumber("August"))
        self.assertFalse(check_monthnumber("October"))
        self.assertFalse(check_monthnumber("December"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnumber(123)
        with self.assertRaises(TypeError):
            check_monthnumber([1, 2, 3])
        with self.assertRaises(TypeError):
            check_monthnumber({"a": 1, "b": 2})
