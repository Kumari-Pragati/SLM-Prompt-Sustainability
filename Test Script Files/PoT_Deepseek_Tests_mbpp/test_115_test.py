import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_typical_case_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_typical_case_non_empty_list(self):
        self.assertFalse(empty_dit([{'a': 1}]))

    def test_edge_case_single_empty_dict(self):
        self.assertTrue(empty_dit([{}]))

    def test_boundary_case_multiple_empty_dicts(self):
        self.assertTrue(empty_dit([{}, {}]))

    def test_corner_case_mixed_dicts_and_non_dicts(self):
        self.assertFalse(empty_dit([{}, 1, 'a', {}]))

    def test_corner_case_empty_dicts_and_non_dicts(self):
        self.assertFalse(empty_dit([{}, 'a', 1]))
