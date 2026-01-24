import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(upper_ctr('HelloWorld'), 2)

    def test_no_uppercase_letters(self):
        self.assertEqual(upper_ctr('helloworld'), 0)

    def test_empty_string(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_all_uppercase_letters(self):
        self.assertEqual(upper_ctr('HELLOWORLD'), 10)

    def test_mixed_case_letters(self):
        self.assertEqual(upper_ctr('HeLlO WoRlD'), 3)

    def test_string_with_special_characters(self):
        self.assertEqual(upper_ctr('Hello@World'), 2)

    def test_string_with_numbers(self):
        self.assertEqual(upper_ctr('Hello123World456'), 2)
