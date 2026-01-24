import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))
        self.assertEqual(max_length_list([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]), (3, ["a", "b", "c"]))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_edge_case_single_element(self):
        self.assertEqual(max_length_list([[1]]), (1, [1]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_length_list(["a"]), (1, "a"))

    def test_boundary_case_one_element_longer(self):
        self.assertEqual(max_length_list([[1, 2], [1, 2, 3]]), (2, [1, 2, 3]))
        self.assertEqual(max_length_list(["a", "b"]), (2, ["a", "b"]))

    def test_corner_case_mixed_types(self):
        self.assertEqual(max_length_list([[1, 2], [1, 2, 3], "abc"]), (3, [1, 2, 3]))
