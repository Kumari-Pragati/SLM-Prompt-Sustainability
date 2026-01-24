import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(remove_parenthesis(["a(b)c"]), ["ac"])
        self.assertEqual(remove_parenthesis(["a(b)c(d)"]), ["ac", "d"])
        self.assertEqual(remove_parenthesis(["a(b)c(d)(e)"]), ["ac", "de"])

    def test_edge_cases(self):
        self.assertEqual(remove_parenthesis(["()"]), [])
        self.assertEqual(remove_parenthesis(["(a)"]), ["a"])
        self.assertEqual(remove_parenthesis(["(a)(b)"]), ["a", "b"])
        self.assertEqual(remove_parenthesis(["(a)(b)(c)"]), ["a", "b", "c"])
        self.assertEqual(remove_parenthesis(["(a)(b)(c)(d)"]), ["a", "b", "c", "d"])

    def test_complex_cases(self):
        self.assertEqual(remove_parenthesis(["a(b(c)d)e"]), ["a", "bce"])
        self.assertEqual(remove_parenthesis(["a(b(c(d)e)f)g"]), ["a", "bcf", "g"])
        self.assertEqual(remove_parenthesis(["a(b(c(d(e)f)g)h)i"]), ["a", "bcfgh", "i"])
