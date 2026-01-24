import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 2), "Hello:world:")

    def test_boundary_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 10), "Hello:world:")

    def test_edge_case(self):
        self.assertEqual(replace_max_specialchar("No special characters here.", 0), "No special characters here.")

    def test_all_special_chars(self):
        self.assertEqual(replace_max_specialchar("., ", 2), "::")

    def test_no_replacement_needed(self):
        self.assertEqual(replace_max_specialchar("No special chars", 2), "No special chars")

    def test_replacement_with_more_than_available(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 3), "Hello:world:")
