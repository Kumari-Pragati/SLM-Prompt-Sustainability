import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_empty_list(self):
        """Checks that an empty list returns an empty string."""
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        """Checks that a single element list returns the expected string."""
        self.assertEqual(concatenate_empty_spaces(["A"]), " A")

    def test_multiple_elements(self):
        """Checks that multiple elements are concatenated correctly."""
        self.assertEqual(concatenate_empty_spaces(["A", "B", "C"]), " A B C")

    def test_mixed_types(self):
        """Checks that non-string elements are converted to strings."""
        self.assertEqual(concatenate_empty_spaces([1, "A", 3.14]), "1 A 3.14")

    def test_whitespace_in_list(self):
        """Checks that whitespace within the list is included in the result."""
        self.assertEqual(concatenate_empty_spaces(["A ", "B"]), "A B")

    def test_large_list(self):
        """Checks that large lists are handled correctly."""
        large_list = ["A" * i for i in range(100)]
        result = concatenate_empty_spaces(large_list)
        self.assertEqual(len(result), sum(1 for _ in large_list))

    def test_negative_list_length(self):
        """Checks that a negative list length raises a ValueError."""
        with self.assertRaises(ValueError):
            concatenate_empty_spaces([][-1])
