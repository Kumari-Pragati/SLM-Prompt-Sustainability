import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(check_Concat("abcabcabc", "abc"))
        self.assertTrue(check_Concat("123123", "123"))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertTrue(check_Concat("", ""))
        self.assertFalse(check_Concat("a", ""))
        self.assertFalse(check_Concat("", "a"))
        self.assertTrue(check_Concat("a", "a"))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(check_Concat("abcabcabc", "abcd"))
        self.assertFalse(check_Concat("abcabcabc", "abcabcabcabc"))
        self.assertFalse(check_Concat("abcabcabc", "ab"))
