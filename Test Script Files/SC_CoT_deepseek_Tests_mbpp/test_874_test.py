import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Concat('abcabcabc', 'abc'))

    def test_edge_case(self):
        self.assertTrue(check_Concat('a', 'a'))
        self.assertFalse(check_Concat('abcabcabc', 'abcd'))

    def test_boundary_case(self):
        self.assertTrue(check_Concat('a'*1000000, 'a'))
        self.assertFalse(check_Concat('a'*1000001, 'a'))

    def test_special_case(self):
        self.assertFalse(check_Concat('abcabcabc', 'ab'))
        self.assertFalse(check_Concat('abcabcabc', 'abcd'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Concat(123, 'abc')
        with self.assertRaises(TypeError):
            check_Concat('abc', 123)
