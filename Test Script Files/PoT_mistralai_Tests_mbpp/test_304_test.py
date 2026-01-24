import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 3), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 4), 5)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 5), 1)

    def test_edge_case_left(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 0), (2, 4)], 1, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 0), (2, 4)], 1, 1), 2)

    def test_edge_case_right(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 2)], 1, 2), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 2)], 1, 3), 2)

    def test_edge_case_out_of_range(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 6), None)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, -1), None)

    def test_empty_array(self):
        self.assertEqual(find_Element([], [(0, 2), (2, 4)], 1, 1), None)

    def test_empty_range(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [], 1, 1), None)
