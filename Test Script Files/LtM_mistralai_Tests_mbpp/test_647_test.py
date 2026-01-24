import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(split_upperstring("ABC"), ["ABC"])
        self.assertListEqual(split_upperstring("aBC"), [])
        self.assertListEqual(split_upperstring("AbCdEf"), ["Ab", "Cd", "Ef"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(split_upperstring("A"), ["A"])
        self.assertListEqual(split_upperstring("AB"), ["AB"])
        self.assertListEqual(split_upperstring("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "UVW", "XYZ"])
        self.assertListEqual(split_upperstring("AaBbCc"), [])
        self.assertListEqual(split_upperstring("ABC_123"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC_123_"), ["ABC"])
        self.assertListEqual(split_upperstring("123ABC"), [])

    def test_complex_scenarios(self):
        self.assertListEqual(split_upperstring("ABC123ABC"), ["ABC", "123", "ABC"])
        self.assertListEqual(split_upperstring("ABC123ABC_123"), ["ABC", "123", "ABC", "123"])
        self.assertListEqual(split_upperstring("ABC123ABC_123_"), ["ABC", "123", "ABC"])
        self.assertListEqual(split_upperstring("ABC_123_ABC"), ["ABC", "123", ""])
        self.assertListEqual(split_upperstring("ABC_123_ABC_"), ["ABC", "123", ""])
