import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(len_log([["a", "b"], ["c", "d"], ["e", "f"]]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_edge_case_single_item(self):
        self.assertEqual(len_log(["abc"]), 3)

    def test_edge_case_single_item_list(self):
        self.assertEqual(len_log([[""]]), 0)

    def test_edge_case_all_same_length(self):
        self.assertEqual(len_log([["a", "b"], ["a", "b"], ["a", "b"]]), 2)

    def test_edge_case_negative_length(self):
        self.assertEqual(len_log([["-1", "-2"], ["-3", "-4"]]), -1)

    def test_edge_case_zero_length(self):
        self.assertEqual(len_log([["", ""], [" ", " "]]), 0)
