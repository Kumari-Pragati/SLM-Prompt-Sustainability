import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sample_nam(["JohnDoe", "janeSmith"]), 2)

    def test_edge_case_uppercase_only(self):
        self.assertEqual(sample_nam(["ABC", "DEF"]), 2)

    def test_edge_case_lowercase_only(self):
        self.assertEqual(sample_nam(["john", "jane"]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_edge_case_single_name(self):
        self.assertEqual(sample_nam(["JohnDoe"]), 1)

    def test_edge_case_mixed_case(self):
        self.assertEqual(sample_nam(["John_Doe", "janeSmith"]), 2)

    def test_corner_case_no_letters(self):
        self.assertEqual(sample_nam(["123", "456"]), 0)

    def test_corner_case_special_characters(self):
        self.assertEqual(sample_nam(["JohnDoe@example.com", "janeSmith#123"]), 2)
