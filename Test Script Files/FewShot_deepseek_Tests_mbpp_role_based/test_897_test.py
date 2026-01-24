import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Word_Present("This is a test sentence", "test"))

    def test_edge_case(self):
        self.assertTrue(is_Word_Present("", ""))

    def test_boundary_case(self):
        self.assertFalse(is_Word_Present("This is a test sentence", ""))

    def test_word_not_present(self):
        self.assertFalse(is_Word_Present("This is a test sentence", "absent"))

    def test_case_sensitivity(self):
        self.assertFalse(is_Word_Present("This is a Test sentence", "test"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Word_Present(123, "test")
        with self.assertRaises(TypeError):
            is_Word_Present("This is a test sentence", 123)
