import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(check_literals("Hello, World!", "World"), "Matched!")
        self.assertEqual(check_literals("Python is awesome!", "awesome"), "Matched!")

    def test_typical_no_match(self):
        self.assertEqual(check_literals("Hello, World!", "Hello"), "Not Matched!")
        self.assertEqual(check_literals("Python is awesome!", "Python"), "Not Matched!")

    def test_edge_case_empty_text(self):
        self.assertEqual(check_literals("", "World"), "Not Matched!")

    def test_edge_case_empty_pattern(self):
        self.assertEqual(check_literals("Hello, World!", ""), "Not Matched!")

    def test_edge_case_single_char_pattern(self):
        self.assertEqual(check_literals("Hello, World!", "!"), "Matched!")
        self.assertEqual(check_literals("Hello, World!", "a"), "Not Matched!")

    def test_corner_case_multi_patterns(self):
        self.assertEqual(check_literals("Hello, World!", ["World", "!"]), "Matched!")
        self.assertEqual(check_literals("Hello, World!", ["World", "a"]), "Not Matched!")
