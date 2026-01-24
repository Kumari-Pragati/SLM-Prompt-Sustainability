import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_uppercase_run_of_length_one(self):
        self.assertEqual(max_run_uppercase('A'), 1)

    def test_uppercase_run_of_length_two(self):
        self.assertEqual(max_run_uppercase('AB'), 1)
        self.assertEqual(max_run_uppercase('BA'), 1)

    def test_uppercase_run_of_length_three_or_more(self):
        self.assertEqual(max_run_uppercase('AAA'), 3)
        self.assertEqual(max_run_uppercase('AAB'), 1)
        self.assertEqual(max_run_uppercase('ABA'), 1)
        self.assertEqual(max_run_uppercase('AAAAA'), 5)

    def test_mixed_case_run_of_length_one(self):
        self.assertEqual(max_run_uppercase('a'), 0)

    def test_mixed_case_run_of_length_two(self):
        self.assertEqual(max_run_uppercase('Ab'), 0)
        self.assertEqual(max_run_uppercase('BA'), 1)

    def test_mixed_case_run_of_length_three_or_more(self):
        self.assertEqual(max_run_uppercase('AaA'), 1)
        self.assertEqual(max_run_uppercase('aAb'), 0)
        self.assertEqual(max_run_uppercase('AbA'), 1)
        self.assertEqual(max_run_uppercase('AaAa'), 1)

    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(''), 0)

    def test_single_uppercase_string(self):
        self.assertEqual(max_run_uppercase('A'), 1)

    def test_single_lowercase_string(self):
        self.assertEqual(max_run_uppercase('a'), 0)
