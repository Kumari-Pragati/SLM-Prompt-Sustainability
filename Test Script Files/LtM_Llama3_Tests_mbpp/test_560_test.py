import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(union_elements((), ()), ())
    def test_single_input(self):
        self.assertEqual(union_elements((1,), ()), (1,))
        self.assertEqual(union_elements((), (2,)), (2,))
    def test_equal_input(self):
        self.assertEqual(union_elements((1, 2), (1, 2)), (1, 2))
    def test_disjoint_input(self):
        self.assertEqual(union_elements((1, 2), (3, 4)), (1, 2, 3, 4))
    def test_intersecting_input(self):
        self.assertEqual(union_elements((1, 2), (2, 3)), (1, 2, 3))
    def test_duplicates_input(self):
        self.assertEqual(union_elements((1, 1, 2), (2, 2, 3)), (1, 2, 3))
