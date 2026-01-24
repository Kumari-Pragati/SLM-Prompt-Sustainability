import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_Concat("abcabcabc", "abc"))

    def test_edge_case(self):
        self.assertTrue(check_Concat("", ""))

    def test_boundary_case(self):
        self.assertFalse(check_Concat("abc", "abcd"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Concat(123, "abc")
