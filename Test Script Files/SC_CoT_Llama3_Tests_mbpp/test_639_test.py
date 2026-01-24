import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sample_nam(['HelloWorld', 'Hello', 'world']), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(sample_nam(['HelloWorld']), 1)

    def test_edge_case_all_uppercase_names(self):
        self.assertEqual(sample_nam(['HELLO', 'WORLD']), 0)

    def test_edge_case_all_lowercase_names(self):
        self.assertEqual(sample_nam(['hello', 'world']), 0)

    def test_edge_case_mixed_case_names(self):
        self.assertEqual(sample_nam(['Hello', 'world']), 2)

    def test_edge_case_names_with_spaces(self):
        self.assertEqual(sample_nam(['Hello World', 'world']), 2)

    def test_edge_case_names_with_punctuation(self):
        self.assertEqual(sample_nam(['Hello,World', 'world']), 2)

    def test_edge_case_names_with_numbers(self):
        self.assertEqual(sample_nam(['Hello123', 'world']), 2)

    def test_edge_case_names_with_special_chars(self):
        self.assertEqual(sample_nam(['Hello!World', 'world']), 2)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sample_nam('hello')

    def test_invalid_input_non_string_elements(self):
        with self.assertRaises(TypeError):
            sample_nam([1, 2, 3])

    def test_invalid_input_non_string_elements_in_list(self):
        with self.assertRaises(TypeError):
            sample_nam(['hello', 2, 'world'])
