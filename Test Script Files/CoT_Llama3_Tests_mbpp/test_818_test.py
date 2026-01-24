import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lower_ctr("hello world"), 7)

    def test_edge_case_empty_string(self):
        self.assertEqual(lower_ctr(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(lower_ctr("a"), 1)

    def test_edge_case_all_uppercase(self):
        self.assertEqual(lower_ctr("HELLO WORLD"), 0)

    def test_edge_case_all_lowercase(self):
        self.assertEqual(lower_ctr("hello world"), 10)

    def test_edge_case_mixed_case(self):
        self.assertEqual(lower_ctr("HeLlO wOrLd"), 6)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            lower_ctr(123)
