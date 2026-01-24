import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(first_Element([1, 2, 3, 4], 4, 1), 1)
        self.assertEqual(first_Element([5, 5, 5, 5], 4, 1), 5)
        self.assertEqual(first_Element([6, 7, 8, 9], 4, 2), 7)

    def test_edge_cases(self):
        self.assertEqual(first_Element([], 0, 1), -1)
        self.assertEqual(first_Element([1], 1, 1), 1)
        self.assertEqual(first_Element([1, 1], 2, 2), 1)
        self.assertEqual(first_Element([1, 2, 1], 3, 2), 1)
        self.assertEqual(first_Element([1, 1, 1, 1], 4, 4), 1)
        self.assertEqual(first_Element([1, 2, 3, 4], 4, 5), -1)

    def test_complex(self):
        self.assertEqual(first_Element([1, 2, 2, 3, 2, 2, 4, 2], 8, 2), 2)
        self.assertEqual(first_Element([0, 0, 1, 0, 0, 1, 0, 0, 1], 9, 1), 0)
        self.assertEqual(first_Element([-1, 0, -1, 1, -1, 0, -1, 1, -1], 9, -1), -1)
