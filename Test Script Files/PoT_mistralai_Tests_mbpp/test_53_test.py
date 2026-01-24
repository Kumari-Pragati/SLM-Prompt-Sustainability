import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_Equality("hello"), "Equal")
        self.assertEqual(check_Equality("A"), "Not Equal")
        self.assertEqual(check_Equality("a"), "Equal")
        self.assertEqual(check_Equality("12345"), "Not Equal")
        self.assertEqual(check_Equality("12321"), "Equal")

    def test_edge_case(self):
        self.assertEqual(check_Equality(""), "Equal")
        self.assertEqual(check_Equality("Aa"), "Equal")
        self.assertEqual(check_Equality("123456"), "Not Equal")
        self.assertEqual(check_Equality("123212"), "Equal")
