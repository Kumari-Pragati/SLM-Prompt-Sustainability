import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(split_upperstring("ABCdefGHIjkl"), ["ABC", "GHI"])
        self.assertListEqual(split_upperstring("ABCdEfGhIjK"), ["ABC", "dEf", "GhI", "jK"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(split_upperstring("A"), ["A"])
        self.assertListEqual(split_upperstring("AB"), ["AB"])
        self.assertListEqual(split_upperstring("AZ"), ["AZ"])
        self.assertListEqual(split_upperstring("ABCXYZ"), ["ABC", "XYZ"])
        self.assertListEqual(split_upperstring(""), [])
        self.assertListEqual(split_upperstring("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRST", "UVW", "XYZ"])

    def test_special_or_corner_cases(self):
        self.assertListEqual(split_upperstring("ABC123"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC-def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC_def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC+def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC@def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC#def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC$def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC^def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC&def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC*def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC(def)"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC)def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC[def]"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC]def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC{def}"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC}def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC|def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC~def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC`def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC'def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC\"def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC\\def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC>def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC<def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC=def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC>="), ["ABC"])
        self.assertListEqual(split_upperstring("ABC<="), ["ABC"])
        self.assertListEqual(split_upperstring("ABC!def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC?def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC:def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC;def"), ["ABC"])
        self.assertListEqual(split_upperstring("ABC,def"), ["ABC"])
        self.assertListEqual