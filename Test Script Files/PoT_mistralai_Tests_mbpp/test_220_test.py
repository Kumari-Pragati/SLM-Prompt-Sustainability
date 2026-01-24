import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello:World:")
        self.assertEqual(replace_max_specialchar("Python, the amazing language!", 3), "Python:the:amazing:language!")

    def test_edge_case_min_length(self):
        self.assertEqual(replace_max_specialchar("", 2), "")
        self.assertEqual(replace_max_specialchar(" ", 2), ":")

    def test_edge_case_max_length(self):
        self.assertEqual(replace_max_specialchar("A" * 100, 2), "A" * 100)

    def test_edge_case_n_larger_than_matches(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 10), "Hello:World!")

    def test_edge_case_n_smaller_than_matches(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello, World!")

    def test_edge_case_non_matching_char(self):
        self.assertEqual(replace_max_specialchar("Hello123, World!", 2), "Hello123, World!")
