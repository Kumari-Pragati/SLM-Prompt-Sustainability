import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(
            remove_similar_row([[1, 2, 3], [3, 2, 1], [1, 2, 4]]),
            [[[1, 2, 3]], [[1, 2, 4]]]
        )

    def test_edge_case_empty_list(self):
        self.assertListEqual(remove_similar_row([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(remove_similar_row([[1, 2, 3]]), [[[1, 2, 3]]])

    def test_edge_case_single_element_duplicate(self):
        self.assertListEqual(remove_similar_row([[[1, 2, 3]]]), [[[1, 2, 3]]])

    def test_edge_case_two_elements_same(self):
        self.assertListEqual(remove_similar_row([[[1, 2, 3]], [[1, 2, 3]]]), [[[1, 2, 3]]])

    def test_edge_case_two_elements_different_order(self):
        self.assertListEqual(
            remove_similar_row([[[1, 2, 3]], [[3, 2, 1]]]),
            [[[1, 2, 3]], [[3, 2, 1]]]
        )

    def test_edge_case_two_elements_different_elements(self):
        self.assertListEqual(
            remove_similar_row([[[1, 2, 3]], [[4, 5, 6]]]),
            [[[1, 2, 3]], [[4, 5, 6]]]
        )

    def test_corner_case_empty_sublist(self):
        self.assertListEqual(
            remove_similar_row([[[], [1, 2, 3]]]),
            [[[1, 2, 3]]]
        )

    def test_corner_case_all_sublists_empty(self):
        self.assertListEqual(remove_similar_row([[]]), [[]])
