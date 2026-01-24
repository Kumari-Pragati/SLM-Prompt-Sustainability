import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(anagram_lambda(["hello", "world", "world"], "world"), ["world"])

    def test_edge_case_empty_string(self):
        self.assertEqual(anagram_lambda(["hello", "world"], ""), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(anagram_lambda([], "world"), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(anagram_lambda(["hello"], "world"), [])

    def test_edge_case_single_element_string(self):
        self.assertEqual(anagram_lambda(["hello"], "hello"), ["hello"])

    def test_edge_case_single_element_string_match(self):
        self.assertEqual(anagram_lambda(["hello"], "hello"), ["hello"])

    def test_edge_case_single_element_string_no_match(self):
        self.assertEqual(anagram_lambda(["hello"], "world"), [])

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(anagram_lambda(["hello", "world", "world"], "world"), ["world", "world"])

    def test_edge_case_multiple_elements_list_no_match(self):
        self.assertEqual(anagram_lambda(["hello", "world", "abc"], "world"), ["world"])

    def test_edge_case_multiple_elements_list_no_match2(self):
        self.assertEqual(anagram_lambda(["hello", "world", "abc", "def"], "world"), ["world"])

    def test_edge_case_multiple_elements_list_no_match3(self):
        self.assertEqual(anagram_lambda(["hello", "world", "abc", "def", "ghi"], "world"), ["world"])
