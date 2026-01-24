import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(''), 0)

    def test_all_uppercase(self):
        self.assertEqual(max_run_uppercase('ABCDEFG'), 7)

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase('AbCdEfG'), 3)

    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase('A'), 1)

    def test_single_lowercase(self):
        self.assertEqual(max_run_uppercase('a'), 0)

    def test_long_string(self):
        self.assertEqual(max_run_uppercase('ThisIsALongStringWithSomeUppercaseLettersInTheMiddle'), 5)

    def test_multiple_runs(self):
        self.assertEqual(max_run_uppercase('AAAAABBBBCCCC'), 6)

    def test_edge_case_start_uppercase(self):
        self.assertEqual(max_run_uppercase('ABC'), 3)

    def test_edge_case_end_uppercase(self):
        self.assertEqual(max_run_uppercase('abcZ'), 2)

    def test_edge_case_start_and_end_uppercase(self):
        self.assertEqual(max_run_uppercase('ABCZ'), 3)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            max_run_uppercase([])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            max_run_uppercase(123)
