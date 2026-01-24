import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_simple_equal_strings(self):
        self.assertEqual(check_Equality("abcd"), "Equal")
        self.assertEqual(check_Equality("abcde"), "Equal")
        self.assertEqual(check_Equality("a"), "Equal")

    def test_simple_not_equal_strings(self):
        self.assertEqual(check_Equality("abc"), "Not Equal")
        self.assertEqual(check_Equality("abcdx"), "Not Equal")
        self.assertEqual(check_Equality(""), "Not Equal")

    def test_edge_cases(self):
        self.assertEqual(check_Equality("A"), "Equal")
        self.assertEqual(check_Equality("aA"), "Equal")
        self.assertEqual(check_Equality("z"), "Equal")
        self.assertEqual(check_Equality("Z"), "Equal")

    def test_complex_cases(self):
        self.assertEqual(check_Equality("abCd"), "Not Equal")
        self.assertEqual(check_Equality("1234"), "Equal")
        self.assertEqual(check_Equality("12345"), "Not Equal")
        self.assertEqual(check_Equality("1234_"), "Equal")
