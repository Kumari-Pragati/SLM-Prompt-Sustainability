import unittest
from mbpp_186_code import escape
from 186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(check_literals("Hello World", ["Hello", "World"]), 'Matched!')

    def test_edge_case_start(self):
        self.assertEqual(check_literals("Hello World", ["World", "Hello"]), 'Matched!')

    def test_edge_case_end(self):
        self.assertEqual(check_literals("Hello World", ["Worlds", "Hello"]), 'Not Matched!')

    def test_edge_case_middle(self):
        self.assertEqual(check_literals("Hello World", ["Worldl", "Hello"]), 'Not Matched!')

    def test_case_insensitive(self):
        self.assertEqual(check_literals("Hello World", ["hello", "world"]), 'Matched!')

    def test_multiple_patterns(self):
        self.assertEqual(check_literals("Hello World", ["Hello", "World", "Worldl"]), 'Matched!')

    def test_empty_patterns(self):
        self.assertEqual(check_literals("Hello World", []), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals("", ["Hello", "World"]), 'Not Matched!')

    def test_special_characters(self):
        self.assertEqual(check_literals("Hello, World!", ["Hello,", "World!"]), 'Matched!')

    def test_escaped_special_characters(self):
        self.assertEqual(check_literals("Hello, World!", [escape("Hello,"), escape("World!")]), 'Matched!')

    def test_invalid_pattern(self):
        with self.assertRaises(TypeError):
            check_literals("Hello World", 123)
