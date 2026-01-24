import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sample_nam(["JohnDoe", "janeSmith"]), 2)

    def test_edge_case_uppercase(self):
        self.assertEqual(sample_nam(["ABCDEF", "abcGHI"]), 1)

    def test_edge_case_lowercase(self):
        self.assertEqual(sample_nam(["johnDoe", "JANESmith"]), 0)

    def test_edge_case_empty(self):
        self.assertEqual(sample_nam([]), 0)

    def test_edge_case_single_word(self):
        self.assertEqual(sample_nam(["Example"]), 0)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(sample_nam(["  John   Doe  "]), 0)

    def test_edge_case_non_alphabetic(self):
        self.assertEqual(sample_nam(["123John", "jane#Smith"]), 0)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            sample_nam([])
