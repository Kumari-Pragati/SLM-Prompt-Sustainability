import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(upper_ctr('HelloWorld'), 2)

    def test_all_uppercase(self):
        self.assertEqual(upper_ctr('HELLO'), 5)

    def test_all_lowercase(self):
        self.assertEqual(upper_ctr('hello'), 0)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr('HeLLoWoRlD'), 3)

    def test_empty_string(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_string_with_numbers(self):
        self.assertEqual(upper_ctr('He12LL3o'), 2)

    def test_string_with_special_characters(self):
        self.assertEqual(upper_ctr('He@LL#o'), 2)
