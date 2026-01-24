import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6], 6), 5)

    def test_edge_case_missing_first(self):
        self.assertEqual(find_missing([2, 3, 4, 5, 6], 6), 1)

    def test_edge_case_missing_last(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 6), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(find_missing([1], 1), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_missing([], 0), -1)

    def test_explicitly_handled_error_case(self):
        with self.assertRaises(TypeError):
            find_missing("not_an_array", 10)
