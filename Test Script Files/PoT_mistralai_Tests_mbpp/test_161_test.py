import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(remove_elements([1, 2, 3, 4, 5], [3, 4]), [1, 2, 5])
        self.assertListEqual(remove_elements(["a", "b", "c", "d"], ["b", "c"]), ["a", "d"])

    def test_edge_case_empty_lists(self):
        self.assertListEqual(remove_elements([], []), [])
        self.assertListEqual(remove_elements([1], []), [1])
        self.assertListEqual(remove_elements([], [1]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(remove_elements([1], [1]), [])
        self.assertListEqual(remove_elements([1], []), [1])

    def test_edge_case_one_in_other(self):
        self.assertListEqual(remove_elements([1], [2]), [1])
        self.assertListEqual(remove_elements([2], [1]), [2])

    def test_corner_case_none_in_other(self):
        self.assertListEqual(remove_elements([1], [2, 3]), [1])
        self.assertListEqual(remove_elements([2, 3], [1]), [2, 3])
