import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(num_position("hello12world34"), 0)
        self.assertEqual(num_position("1234567890"), 0)
        self.assertEqual(num_position("a1b2c3d4"), 0)
        self.assertEqual(num_position("1a2b3c4d"), 1)
        self.assertEqual(num_position("12a3b4c5"), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(num_position(""), -1)
        self.assertEqual(num_position("0"), 0)
        self.assertEqual(num_position("12345678901"), 10)
        self.assertEqual(num_position("123456789012"), 10)
        self.assertEqual(num_position("1234567890123"), 10)
        self.assertEqual(num_position("12345678901234"), 10)
        self.assertEqual(num_position("123456789012345"), 10)
        self.assertEqual(num_position("1234567890123456"), 10)
        self.assertEqual(num_position("12345678901234567"), 10)
        self.assertEqual(num_position("123456789012345678"), 10)
        self.assertEqual(num_position("1234567890123456789"), 10)
        self.assertEqual(num_position("12345678901234567890"), 10)

    def test_special_cases(self):
        self.assertEqual(num_position("123-456"), 0)
        self.assertEqual(num_position("123.456"), -1)
        self.assertEqual(num_position("123$456"), -1)
        self.assertEqual(num_position("123%456"), -1)
        self.assertEqual(num_position("123+456"), -1)
        self.assertEqual(num_position("123@456"), -1)
        self.assertEqual(num_position("123#456"), -1)
        self.assertEqual(num_position("123^456"), -1)
        self.assertEqual(num_position("123&456"), -1)
        self.assertEqual(num_position("123*456"), -1)
        self.assertEqual(num_position("123("), -1)
        self.assertEqual(num_position("123)"), -1)
        self.assertEqual(num_position("123["), -1)
        self.assertEqual(num_position("123]"), -1)
        self.assertEqual(num_position("123{"), -1)
        self.assertEqual(num_position("123}"), -1)
        self.assertEqual(num_position("123|"), -1)
        self.assertEqual(num_position("123~"), -1)
        self.assertEqual(num_position("123`"), -1)
        self.assertEqual(num_position("123'"), -1)
        self.assertEqual(num_position("123\""), -1)
        self.assertEqual(num_position("123!"), -1)
        self.assertEqual(num_position("123:"), -1)
        self.assertEqual(num_position("123;"), -1)
        self.assertEqual(num_position("123<"), -1)
        self.assertEqual(num_position("123>"), -1)
        self.assertEqual(num_position("12