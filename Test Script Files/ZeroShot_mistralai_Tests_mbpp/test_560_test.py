import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_union_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_union_single_element_tuples(self):
        self.assertEqual(union_elements((1,), (1,)), (1,))
        self.assertEqual(union_elements(('a',), ('a',)), ('a',))

    def test_union_overlapping_tuples(self):
        self.assertEqual(union_elements((1, 2, 3), (2, 4, 3)), (1, 2, 3, 4))
        self.assertEqual(union_elements(('a', 'b', 'c'), ('b', 'd', 'c')), ('a', 'b', 'c', 'd'))

    def test_union_non_overlapping_tuples(self):
        self.assertEqual(union_elements((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(union_elements(('a', 'b', 'c'), ('d', 'e', 'f')), ('a', 'b', 'c', 'd', 'e', 'f'))
