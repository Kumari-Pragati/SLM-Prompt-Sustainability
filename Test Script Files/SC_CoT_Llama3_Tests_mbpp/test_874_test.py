import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(check_Concat("abc", "ab"))
        self.assertTrue(check_Concat("abc", "abc"))
        self.assertTrue(check_Concat("abc", "abcabc"))

    def test_edge_cases(self):
        self.assertFalse(check_Concat("abc", "a"))
        self.assertFalse(check_Concat("abc", "abcabcabc"))
        self.assertFalse(check_Concat("abc", "abcabcabcabc"))

    def test_special_cases(self):
        self.assertTrue(check_Concat("abc", ""))
        self.assertTrue(check_Concat("", "abc"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Concat(None, "abc")
        with self.assertRaises(TypeError):
            check_Concat("abc", None)
        with self.assertRaises(TypeError):
            check_Concat("", None)
        with self.assertRaises(TypeError):
            check_Concat(None, "")

    def test_empty_strings(self):
        self.assertTrue(check_Concat("", ""))
        self.assertTrue(check_Concat("abc", ""))
