import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(lower_ctr('hello'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(lower_ctr(''), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(lower_ctr('a'), 1)

    def test_edge_case_all_uppercase(self):
        self.assertEqual(lower_ctr('HELLO'), 0)

    def test_edge_case_all_lowercase(self):
        self.assertEqual(lower_ctr('hello'), 5)

    def test_edge_case_mixed_case(self):
        self.assertEqual(lower_ctr('HeLlO'), 3)

    def test_edge_case_non_alpha_chars(self):
        self.assertEqual(lower_ctr('Hello123'), 2)

    def test_edge_case_non_alpha_chars_and_spaces(self):
        self.assertEqual(lower_ctr('Hello 123'), 2)

    def test_edge_case_non_alpha_chars_and_punctuation(self):
        self.assertEqual(lower_ctr('Hello!123'), 2)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            lower_ctr(123)
