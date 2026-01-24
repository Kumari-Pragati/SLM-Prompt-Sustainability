import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):

    def test_typical_case_list(self):
        self.assertEqual(find_lists(['a', 'b', 'c']), 1)

    def test_typical_case_non_list(self):
        self.assertEqual(find_lists('abc'), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_lists([]), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(find_lists(''), 0)

    def test_corner_case_single_element_list(self):
        self.assertEqual(find_lists(['a']), 1)

    def test_corner_case_single_character_string(self):
        self.assertEqual(find_lists('a'), 1)
