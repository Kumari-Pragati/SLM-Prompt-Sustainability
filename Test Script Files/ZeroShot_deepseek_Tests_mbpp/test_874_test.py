import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_valid_concatenation(self):
        self.assertTrue(check_Concat('abcabcabc', 'abc'))
        self.assertTrue(check_Concat('123123', '123'))
        self.assertTrue(check_Concat('hellohello', 'hello'))

    def test_invalid_concatenation(self):
        self.assertFalse(check_Concat('abcabcabcabc', 'abc'))
        self.assertFalse(check_Concat('1231231', '123'))
        self.assertFalse(check_Concat('hellohelloworld', 'hello'))

    def test_empty_strings(self):
        self.assertTrue(check_Concat('', ''))

    def test_single_character_strings(self):
        self.assertTrue(check_Concat('a', 'a'))
        self.assertFalse(check_Concat('a', 'b'))
