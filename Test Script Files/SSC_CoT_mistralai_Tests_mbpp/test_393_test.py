import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))
        self.assertEqual(max_length_list([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]) , (3, ["a", "b", "c"]))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_length_list([[]]), (0, []))
        self.assertEqual(max_length_list([[1]]), (1, [1]))
        self.assertEqual(max_length_list([[1], [2]]), (2, [2]))
        self.assertEqual(max_length_list([[1], [2], [3]]), (3, [1, 2, 3]))
        self.assertEqual(max_length_list([[1], [2, 3], [4, 5, 6]]), (3, [2, 3]))
        self.assertEqual(max_length_list([[1, 2], [3, 4], [5, 6, 7]]), (3, [1, 2]))

    def test_special_or_corner_cases(self):
        self.assertEqual(max_length_list([[1], [2, 3], [2, 3]]), (2, [2, 3]))
        self.assertEqual(max_length_list([["a"], ["b", "c"], ["b", "d"]]), (2, ["b", "c"]))
        self.assertEqual(max_length_list([[1], [2, 3], [2, 3, 4]]), (3, [2, 3, 4]))
