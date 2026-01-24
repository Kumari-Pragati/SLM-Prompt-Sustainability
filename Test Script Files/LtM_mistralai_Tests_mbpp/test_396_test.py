import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_simple_single_char(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("z"), "Valid")

    def test_simple_multi_char(self):
        self.assertEqual(check_char("abcd"), "Invalid")
        self.assertEqual(check_char("abcde"), "Invalid")
        self.assertEqual(check_char("zabc"), "Invalid")

    def test_edge_cases(self):
        self.assertEqual(check_char("A"), "Invalid")
        self.assertEqual(check_char("0"), "Invalid")
        self.assertEqual(check_char("_"), "Invalid")
        self.assertEqual(check_char(" "), "Invalid")

    def test_complex_cases(self):
        self.assertEqual(check_char("az"), "Valid")
        self.assertEqual(check_char("zaz"), "Valid")
        self.assertEqual(check_char("zazaz"), "Invalid")
