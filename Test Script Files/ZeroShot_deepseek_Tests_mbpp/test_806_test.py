import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_all_uppercase(self):
        self.assertEqual(max_run_uppercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_all_lowercase(self):
        self.assertEqual(max_run_uppercase('abcdefghijklmnopqrstuvwxyz'), 0)

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase('AbCDeFgHiJkLmNoPqRsTuVwXyZ'), 26)

    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase('A'), 1)

    def test_single_lowercase(self):
        self.assertEqual(max_run_uppercase('a'), 0)

    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(''), 0)

    def test_all_uppercase_with_spaces(self):
        self.assertEqual(max_run_uppercase('ABC DEF GHI JKL MNO PQR STU VWX YZ'), 26)

    def test_all_uppercase_with_special_chars(self):
        self.assertEqual(max_run_uppercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'), 26)
