import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(check_literals("Hello, World!", "World"), "Matched!")

    def test_case_sensitivity(self):
        self.assertEqual(check_literals("Hello, World!", "world"), "Not Matched!")
        self.assertEqual(check_literals("Hello, World!", "WORLD"), "Not Matched!")

    def test_multiple_patterns(self):
        self.assertEqual(check_literals("Hello, World!", ["World", "Hello"]), "Matched! Matched!")

    def test_empty_patterns(self):
        self.assertEqual(check_literals("Hello, World!", []), "Not Matched!")

    def test_empty_text(self):
        self.assertEqual(check_literals("", ["World"]), "Not Matched!")

    def test_no_match(self):
        self.assertEqual(check_literals("Hello, World!", ["123"]), "Not Matched!")
