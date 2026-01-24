import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5], 11), 4)

    def test_edge_case(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_boundary_case(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5], 10), 4)

    def test_special_case(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Diff("1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5", 11)
        with self.assertRaises(TypeError):
            find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5], "11")
        with self.assertRaises(TypeError):
            find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, "5"], 11)
