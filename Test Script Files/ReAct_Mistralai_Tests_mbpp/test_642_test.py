import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertSetEqual(set(), remove_similar_row([]))

    def test_single_element_list(self):
        self.assertSetEqual({(1, 2, 3)}, remove_similar_row([(1, 2, 3)]))

    def test_identical_rows(self):
        self.assertSetEqual({(1, 2, 3), (1, 2, 3)}, remove_similar_row([(1, 2, 3), (1, 2, 3)]))

    def test_different_orders(self):
        self.assertSetEqual({(1, 2, 3), (3, 2, 1)}, remove_similar_row([(1, 2, 3), (3, 2, 1)]))

    def test_duplicate_elements(self):
        self.assertSetEqual({(1, 2, 2), (1, 2, 3)}, remove_similar_row([(1, 2, 2), (1, 2, 3)]))

    def test_empty_sublists(self):
        self.assertSetEqual({(1,), (2,), (3,)}, remove_similar_row([(1,), (2,), (3,)]))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            remove_similar_row([(1, 2, 3), (1, '2', 3)])

    def test_nested_lists(self):
        self.assertSetEqual({(1, (2, 3)), ((1, 2), 3)}, remove_similar_row([(1, (2, 3)), ((1, 2), 3)]))
