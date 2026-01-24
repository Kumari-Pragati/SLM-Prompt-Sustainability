import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello, World!"
        patterns = ["World", "Python"]
        self.assertEqual(check_literals(text, patterns), 'Matched!')

    def test_edge_condition(self):
        text = ""
        patterns = ["World", "Python"]
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_boundary_condition(self):
        text = "Hello, World!"
        patterns = []
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_invalid_input(self):
        text = 12345
        patterns = ["World", "Python"]
        with self.assertRaises(TypeError):
            check_literals(text, patterns)
