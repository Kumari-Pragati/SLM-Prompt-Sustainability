import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(remove_Char("Hello", "l"), "Heo")
        self.assertEqual(remove_Char("Python", "n"), "Pytho")
        self.assertEqual(remove_Char("SpamSpamSpam", "a"), "SpmSpmSpm")

    def test_edge_cases(self):
        self.assertEqual(remove_Char("", "a"), "")
        self.assertEqual(remove_Char("a", "a"), "")
        self.assertEqual(remove_Char("abc", "d"), "abc")
        self.assertEqual(remove_Char("abc", "z"), "abc")

    def test_boundary_cases(self):
        self.assertEqual(remove_Char("A", "a"), "")
        self.assertEqual(remove_Char("a", "A"), "")
        self.assertEqual(remove_Char("Aa", "a"), "")
        self.assertEqual(remove_Char("aa", "A"), "")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_Char, 1, "a")
        self.assertRaises(TypeError, remove_Char, "Hello", 1)
