import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertEqual(concatenate_strings((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(concatenate_strings(("a",), ("b",)), ("ab",))

    def test_tuples_of_equal_length(self):
        self.assertEqual(concatenate_strings(("a", "b", "c"), ("d", "e", "f")), ("ad", "be", "cf"))

    def test_tuples_of_different_lengths(self):
        self.assertEqual(concatenate_strings(("a", "b"), ("c", "d", "e")), ("ac", "bd"))

    def test_tuples_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate_strings((1, 2), ("a", "b"))

    def test_tuples_with_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate_strings(("a", 2), ("b", "c"))
