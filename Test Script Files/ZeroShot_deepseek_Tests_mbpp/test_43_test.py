import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match('abc_def'), 'Found a match!')
        self.assertEqual(text_match('ghi_jkl'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('abc_defg'), 'Not matched!')
        self.assertEqual(text_match('ghi_jklm'), 'Not matched!')
        self.assertEqual(text_match('123_456'), 'Not matched!')
        self.assertEqual(text_match('Abc_Def'), 'Not matched!')
        self.assertEqual(text_match('ghi_jkl_mno'), 'Not matched!')
