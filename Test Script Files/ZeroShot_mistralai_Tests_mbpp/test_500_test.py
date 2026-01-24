import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), "")

    def test_single_element(self):
        self.assertEqual(concatenate_elements(["a"]), "a")

    def test_multiple_elements(self):
        self.assertEqual(concatenate_elements(["a", "b", "c"]), "abc")

    def test_mixed_types(self):
        self.assertEqual(concatenate_elements(["a", 1, "b"]), "a1b")

    def test_empty_string(self):
        self.assertEqual(concatenate_elements(["", "b"]), "b")
