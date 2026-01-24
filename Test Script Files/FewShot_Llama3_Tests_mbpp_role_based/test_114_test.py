import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        expected_output = "[(1, 1), (2, 2), (3, 3), (4, 4)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_edge_case_empty_list(self):
        test_list = []
        expected_output = "[]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_edge_case_single_element_list(self):
        test_list = [1]
        expected_output = "[(1, 1)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_edge_case_duplicates(self):
        test_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        expected_output = "[(1, 2), (2, 3), (3, 4), (4, 5)]"
        self.assertEqual(assign_freq(test_list), expected_output)
