import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5]))
        self.assertTrue(all_unique(["a", "b", "c", "d", "e"]))
        self.assertTrue(all_unique([1.0, 2.0, 3.0, 4.0, 5.0]))

    def test_edge_case_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_edge_case_single_element(self):
        self.assertTrue(all_unique([1]))
        self.assertTrue(all_unique(["a"]))
        self.assertTrue(all_unique([1.0]))

    def test_edge_case_duplicates(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 4, 5]))
        self.assertFalse(all_unique(["a", "a", "b", "c", "d", "e"]))
        self.assertFalse(all_unique([1.0, 1.0, 2.0, 3.0, 4.0, 5.0]))

    def test_corner_case_none(self):
        self.assertRaises(TypeError, all_unique, None)

    def test_corner_case_set(self):
        self.assertTrue(all_unique(set([1, 2, 3, 4, 5])))
        self.assertTrue(all_unique(set(["a", "b", "c", "d", "e"])))
        self.assertTrue(all_unique(set([1.0, 2.0, 3.0, 4.0, 5.0])))
