import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 3), 1)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_X((), 1), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching(self):
        self.assertEqual(count_X((1,), 2), 0)

    def test_edge_case_single_element_tuple_matching(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_again(self):
        self.assertEqual(count_X((1,), 3), 0)

    def test_edge_case_single_element_tuple_matching_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again(self):
        self.assertEqual(count_X((1,), 4), 0)

    def test_edge_case_single_element_tuple_matching_yet_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again(self):
        self.assertEqual(count_X((1,), 5), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again(self):
        self.assertEqual(count_X((1,), 6), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again(self):
        self.assertEqual(count_X((1,), 7), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 8), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 9), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 10), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 11), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 12), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 13), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 14), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single_element_tuple_non_matching_yet_again_again_again_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 15), 0)

    def test_edge_case_single_element_tuple_matching_yet_again_again_again_again_again_again_again_again_again_again_again_again(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_single