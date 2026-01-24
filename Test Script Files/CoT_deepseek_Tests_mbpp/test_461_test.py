import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(upper_ctr('HelloWorld'), 2)

    def test_empty_string(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_all_upper_case(self):
        self.assertEqual(upper_ctr('HELLO'), 5)

    def test_all_lower_case(self):
        self.assertEqual(upper_ctr('hello'), 0)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr('HeLlO'), 2)

    def test_numeric_string(self):
        self.assertEqual(upper_ctr('123456'), 0)

    def test_special_characters(self):
        self.assertEqual(upper_ctr('@#$%^&*'), 0)

    def test_whitespace(self):
        self.assertEqual(upper_ctr(' '), 0)
