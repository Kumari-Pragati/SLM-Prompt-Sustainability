import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_input(self):
        self.assertListEqual(find_char_long("HelloWorld1234"), ["Hello", "World"])
        self.assertListEqual(find_char_long("AbCdEfGhIjKlMnOpQrStUvWxYz"), ["AbCd", "EfGh", "IjKl", "MnOp", "QrSt", "UvWx", "Yz"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(find_char_long("A"), [])
        self.assertListEqual(find_char_long("AaBbCcDdEe"), ["AaBb", "CcDd", "Ee"])
        self.assertListEqual(find_char_long("A1234"), [])
        self.assertListEqual(find_char_long("A12345"), [])
        self.assertListEqual(find_char_long("A123456"), ["A1234"])
        self.assertListEqual(find_char_long("A1234567"), ["A1234", "567"])
        self.assertListEqual(find_char_long("A12345678"), ["A1234", "5678"])
        self.assertListEqual(find_char_long("A123456789"), ["A1234", "56789"])
        self.assertListEqual(find_char_long("A1234567890"), ["A1234", "567890"])

    def test_invalid_input(self):
        self.assertRaises(ValueError, find_char_long, "")
        self.assertRaises(ValueError, find_char_long, None)
        self.assertRaises(ValueError, find_char_long, 123)
