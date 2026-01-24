import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertListEqual(find_char("HelloWorld"), ["Hello", "World"])
        self.assertListEqual(find_char("PythonProgramming"), ["Python", "Program", "ming"])

    def test_edge_cases(self):
        self.assertListEqual(find_char("AbcdEfGhIjKlMnOpQrStUvWxYz"), ["AbcdE", "FgHijKl", "MnOpQr", "StUvWx", "Yz"])
        self.assertListEqual(find_char("A123B456C789"), ["A123", "B456", "C789"])
        self.assertListEqual(find_char("A_123_B_456_C_789"), ["A_123", "B_456", "C_789"])

    def test_boundary_conditions(self):
        self.assertListEqual(find_char(""), [])
        self.assertListEqual(find_char("A"), ["A"])
        self.assertListEqual(find_char("AAAAA"), ["AAAAA"])
        self.assertListEqual(find_char("AABBCC"), ["AAB", "BBCC"])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_char, 123)
        self.assertRaises(TypeError, find_char, None)
        self.assertRaises(TypeError, find_char, [])
