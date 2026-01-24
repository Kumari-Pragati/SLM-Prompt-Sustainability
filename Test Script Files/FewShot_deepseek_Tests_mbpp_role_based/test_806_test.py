import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_run_uppercase('ABCDE'), 5)

    def test_edge_case(self):
        self.assertEqual(max_run_uppercase(''), 0)

    def test_boundary_case(self):
        self.assertEqual(max_run_uppercase('A'), 1)

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase('ABcDeF'), 3)

    def test_all_lowercase(self):
        self.assertEqual(max_run_uppercase('abcdef'), 0)

    def test_all_uppercase(self):
        self.assertEqual(max_run_uppercase('ABCDEF'), 6)

    def test_mixed_uppercase_lowercase(self):
        self.assertEqual(max_run_uppercase('AbCDeFg'), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_run_uppercase(12345)
