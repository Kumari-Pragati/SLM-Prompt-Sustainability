import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_typical_case(self):
        text = "Hello, World!"
        patterns = ["World"]
        self.assertEqual(check_literals(text, patterns), 'Matched!')

    def test_no_match(self):
        text = "Hello, World!"
        patterns = ["Python"]
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_multiple_patterns(self):
        text = "Hello, World!"
        patterns = ["World", "Python"]
        self.assertEqual(check_literals(text, patterns), 'Matched!')

    def test_empty_text(self):
        text = ""
        patterns = ["World"]
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_empty_patterns(self):
        text = "Hello, World!"
        patterns = []
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_none_text(self):
        text = None
        patterns = ["World"]
        with self.assertRaises(TypeError):
            check_literals(text, patterns)

    def test_none_patterns(self):
        text = "Hello, World!"
        patterns = None
        with self.assertRaises(TypeError):
            check_literals(text, patterns)
