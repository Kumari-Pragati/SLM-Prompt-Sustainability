import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(check_Equality("abcdefg"), "Equal")
        self.assertEqual(check_Equality("ABCDEFG"), "Equal")
        self.assertEqual(check_Equality("123456"), "Equal")
        self.assertEqual(check_Equality("!@#$%^&*()"), "Equal")

    def test_edge_cases(self):
        self.assertEqual(check_Equality(""), "Equal")
        self.assertEqual(check_Equality("a"), "Not Equal")
        self.assertEqual(check_Equality("aaaaaaa"), "Equal")
        self.assertEqual(check_Equality("zzzzzzz"), "Equal")

    def test_boundary_cases(self):
        self.assertEqual(check_Equality("A"), "Not Equal")
        self.assertEqual(check_Equality("Z"), "Not Equal")
        self.assertEqual(check_Equality("0"), "Equal")
        self.assertEqual(check_Equality("9"), "Equal")
