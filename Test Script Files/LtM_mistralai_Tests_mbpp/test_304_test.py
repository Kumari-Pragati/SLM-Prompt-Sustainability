import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 1), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 3), 4)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 0), 1)

    def test_edge_cases(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 0, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 0, 1), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 0, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 0, 3), None)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 6), None)

        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 2, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 2, 1), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 2, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 2, 3), 4)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 2, 6), None)

        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 3, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 3, 1), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 3, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 3, 3), 4)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 3, 6), None)

        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 4, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2,