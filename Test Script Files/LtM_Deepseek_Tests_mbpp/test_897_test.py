import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_simple_present(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_simple_absent(self):
        self.assertFalse(is_Word_Present("Hello World", "Universe"))

    def test_edge_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))

    def test_edge_empty_word(self):
        self.assertFalse(is_Word_Present("Hello World", ""))

    def test_boundary_single_word(self):
        self.assertTrue(is_Word_Present("Hello", "Hello"))

    def test_complex_case_case_sensitivity(self):
        self.assertFalse(is_Word_Present("Hello World", "world"))

    def test_complex_case_multiple_spaces(self):
        self.assertTrue(is_Word_Present("Hello   World", "World"))

    def test_complex_case_trailing_spaces(self):
        self.assertTrue(is_Word_Present("Hello World   ", "World"))
