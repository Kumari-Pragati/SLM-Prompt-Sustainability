import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(get_Char("a"), 'a')
        self.assertEqual(get_Char("z"), 'z')
        self.assertEqual(get_Char("b"), 'b')
        self.assertEqual(get_Char("y"), 'y')
        self.assertEqual(get_Char("c"), 'c')
        self.assertEqual(get_Char("x"), 'x')
        self.assertEqual(get_Char("d"), 'd')
        self.assertEqual(get_Char("w"), 'w')
        self.assertEqual(get_Char("e"), 'e')
        self.assertEqual(get_Char("v"), 'v')
        self.assertEqual(get_Char("f"), 'f')
        self.assertEqual(get_Char("u"), 'u')
        self.assertEqual(get_Char("g"), 'g')
        self.assertEqual(get_Char("t"), 't')
        self.assertEqual(get_Char("h"), 'h')
        self.assertEqual(get_Char("s"),'s')
        self.assertEqual(get_Char("r"), 'r')
        self.assertEqual(get_Char("q"), 'q')
        self.assertEqual(get_Char("p"), 'p')
        self.assertEqual(get_Char("o"), 'o')
        self.assertEqual(get_Char("n"), 'n')
        self.assertEqual(get_Char("m"),'m')
        self.assertEqual(get_Char("l"), 'l')
        self.assertEqual(get_Char("k"), 'k')
        self.assertEqual(get_Char("j"), 'j')
        self.assertEqual(get_Char("i"), 'i')
        self.assertEqual(get_Char("h"), 'h')
        self.assertEqual(get_Char("g"), 'g')
        self.assertEqual(get_Char("f"), 'f')
        self.assertEqual(get_Char("e"), 'e')
        self.assertEqual(get_Char("d"), 'd')
        self.assertEqual(get_Char("c"), 'c')
        self.assertEqual(get_Char("b"), 'b')
        self.assertEqual(get_Char("a"), 'a')

    def test_edge_cases(self):
        self.assertEqual(get_Char(""), None)
        self.assertEqual(get_Char("abc"), 'c')
        self.assertEqual(get_Char("xyz"), 'z')
        self.assertEqual(get_Char("abcxyz"), 'z')

    def test_special_cases(self):
        self.assertEqual(get_Char("abcdefghijklmnopqrstuvwxyz"), 'z')
        self.assertEqual(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), 'z')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_Char(123)
