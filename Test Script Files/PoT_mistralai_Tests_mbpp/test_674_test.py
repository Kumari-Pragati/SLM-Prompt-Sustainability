import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_duplicate("apple apple banana cherry apple"), "apple banana cherry")

    def test_edge_case_single_word(self):
        self.assertEqual(remove_duplicate("apple"), "apple")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_edge_case_whitespace(self):
        self.assertEqual(remove_duplicate("   "), "")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_duplicate("apple apple   banana    cherry   apple"), "apple banana cherry")

    def test_corner_case_duplicate_spaces(self):
        self.assertEqual(remove_duplicate("apple apple  "), "apple")

    def test_corner_case_mixed_case(self):
        self.assertEqual(remove_duplicate("Apple aPPle bAnana CHERRY Apple aPpLe"), "Apple bAnana CHERRY")
