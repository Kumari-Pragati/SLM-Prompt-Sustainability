import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 5), 5)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 0), -1)

    def test_edge2(self):
        self.assertEqual(first_Element([], 0, 1), -1)
        self.assertEqual(first_Element([1], 1, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 6), -1)

    def test_edge3(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 3), 3)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 4), 4)

    def test_edge4(self):
        self.assertEqual(first_Element([1, 1, 1, 1, 1], 5, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 5), 5)
