import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_all_uppercase(self):
        self.assertEqual(upper_ctr('HELLO'), 5)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr('HeLloWoRlD'), 3)

    def test_single_uppercase(self):
        self.assertEqual(upper_ctr('aBc'), 1)

    def test_special_characters(self):
        self.assertEqual(upper_ctr('A1B2C3'), 1)

    def test_whitespace(self):
        self.assertEqual(upper_ctr(' A B C '), 3)
