import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(odd_values_string("abcdefg"), "acfg")
        self.assertEqual(odd_values_string("ABCDEFG"), "ABEG")
        self.assertEqual(odd_values_string("1234567"), "1357")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_values_string(""), "")
        self.assertEqual(odd_values_string("a"), "a")
        self.assertEqual(odd_values_string("ab"), "b")
        self.assertEqual(odd_values_string("abc"), "ac")
        self.assertEqual(odd_values_string("abcdefg"), "acfg")
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "adghijklmnpqrstuvwxyz")
        self.assertEqual(odd_values_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABEGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(odd_values_string("1234567890"), "13579")

    def test_complex_scenarios(self):
        self.assertEqual(odd_values_string("a1b2c3"), "1c3")
        self.assertEqual(odd_values_string("a1b2c3d4"), "1c3d")
        self.assertEqual(odd_values_string("a1b2c3d4e5"), "1c3d5")
        self.assertEqual(odd_values_string("a1b2c3d4e5f6"), "1c3d5f6")
        self.assertEqual(odd_values_string("a1b2c3d4e5f6g7"), "1c3d5f6g7")
        self.assertEqual(odd_values_string("a1b2c3d4e5f6g7h8"), "1c3d5f6g7h8")
