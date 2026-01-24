import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(first_Element([1, 7, 4, 3, 4, 8, 7], 7, 2), 7)

    def test_edge_boundary_conditions(self):
        self.assertEqual(first_Element([], 0, 1), -1)
        self.assertEqual(first_Element([1], 1, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1], 5, 5), 1)

    def test_complex_cases(self):
        self.assertEqual(first_Element([1, 2, 2, 1], 4, 2), 2)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 2), 2)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10), -1)
