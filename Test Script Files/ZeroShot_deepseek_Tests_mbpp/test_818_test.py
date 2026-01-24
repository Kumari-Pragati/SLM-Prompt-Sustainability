import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_lower_ctr_with_lowercase_letters(self):
        self.assertEqual(lower_ctr('abc'), 3)

    def test_lower_ctr_with_uppercase_letters(self):
        self.assertEqual(lower_ctr('ABC'), 0)

    def test_lower_ctr_with_mixed_case_letters(self):
        self.assertEqual(lower_ctr('AbC'), 2)

    def test_lower_ctr_with_numbers(self):
        self.assertEqual(lower_ctr('123'), 0)

    def test_lower_ctr_with_special_characters(self):
        self.assertEqual(lower_ctr('@#$'), 0)

    def test_lower_ctr_with_empty_string(self):
        self.assertEqual(lower_ctr(''), 0)
