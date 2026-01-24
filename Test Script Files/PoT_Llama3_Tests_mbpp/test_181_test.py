import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(common_prefix(["hello", "hello world", "hello again"], 3), "hello")

    def test_edge_case_empty_array(self):
        self.assertEqual(common_prefix([], 0), "")

    def test_edge_case_single_element_array(self):
        self.assertEqual(common_prefix(["hello"], 1), "hello")

    def test_edge_case_two_elements_array(self):
        self.assertEqual(common_prefix(["hello", "hi"], 2), "hi")

    def test_edge_case_all_elements_same(self):
        self.assertEqual(common_prefix(["hello", "hello", "hello"], 3), "hello")

    def test_edge_case_all_elements_empty(self):
        self.assertEqual(common_prefix(["", "", ""], 3), "")

    def test_edge_case_all_elements_single_character(self):
        self.assertEqual(common_prefix(["a", "a", "a"], 3), "a")

    def test_edge_case_all_elements_empty_string(self):
        self.assertEqual(common_prefix(["", "a", "a"], 3), "")

    def test_edge_case_all_elements_single_character_empty(self):
        self.assertEqual(common_prefix(["", "a", ""], 3), "")

    def test_edge_case_all_elements_single_character_single_character(self):
        self.assertEqual(common_prefix(["a", "b", "c"], 3), "")

    def test_edge_case_all_elements_single_character_single_character_empty(self):
        self.assertEqual(common_prefix(["a", "b", ""], 3), "")
