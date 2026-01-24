import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 7, 9], 5), 2)

    def test_edge_case(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Min_Diff([5, 5, 5, 5, 5], 5), 0)

    def test_edge_case3(self):
        self.assertEqual(find_Min_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Min_Diff("hello", 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_Min_Diff([1, 2, 3], "five")
