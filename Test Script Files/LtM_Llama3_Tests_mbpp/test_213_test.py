import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(concatenate_strings((), ()), ())
    def test_single_element_input(self):
        self.assertEqual(concatenate_strings(("a",), ("b",)), ("ab",))
    def test_equal_length_input(self):
        self.assertEqual(concatenate_strings(("a", "b", "c"), ("d", "e", "f")), ("ad", "be", "cf"))
    def test_unequal_length_input(self):
        self.assertEqual(concatenate_strings(("a", "b", "c"), ("d", "e")), ("ad", "be"))
    def test_empty_input_with_non_empty_input(self):
        self.assertEqual(concatenate_strings((), ("a", "b", "c")), ())
    def test_non_empty_input_with_empty_input(self):
        self.assertEqual(concatenate_strings(("a", "b", "c"), ()), ())
    def test_input_with_repeated_elements(self):
        self.assertEqual(concatenate_strings(("a", "a", "b", "c"), ("d", "e", "f")), ("ad", "ae", "cf"))
    def test_input_with_repeated_elements_and_empty_input(self):
        self.assertEqual(concatenate_strings(("a", "a", "b", "c"), ()), ("",))
