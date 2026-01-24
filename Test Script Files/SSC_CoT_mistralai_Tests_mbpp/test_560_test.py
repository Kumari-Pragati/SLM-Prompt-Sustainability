import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_union_normal(self):
        self.assertListEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertListEqual(union_elements(('a', 'b', 'c'), ('c', 'd', 'e')), ('a', 'b', 'c', 'd', 'e'))

    def test_union_edge_cases(self):
        self.assertListEqual(union_elements((1, 2, 3), (3, )), (1, 2, 3))
        self.assertListEqual(union_elements((1, 2, 3), (3, 3, 4)), (1, 2, 4))
        self.assertListEqual(union_elements(('a', 'b', 'c'), ('c', )), ('a', 'b'))
        self.assertListEqual(union_elements(('a', 'b', 'c'), ('c', 'c', 'd')), ('a', 'b', 'd'))

    def test_union_empty(self):
        self.assertListEqual(union_elements((), (1, 2, 3)), (1, 2, 3))
        self.assertListEqual(union_elements((1, 2, 3), ()), (1, 2, 3))
        self.assertListEqual(union_elements((), ()), ())

    def test_union_none(self):
        self.assertIsNone(union_elements(None, (1, 2, 3)))
        self.assertIsNone(union_elements((1, 2, 3), None))
