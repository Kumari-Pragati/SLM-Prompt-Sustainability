import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(union_elements(('a', 'b', 'c'), ('c', 'd', 'e')), ('a', 'b', 'c', 'd', 'e'))

    def test_empty_case(self):
        self.assertEqual(union_elements((), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(union_elements((1, 2, 3),()), (1, 2, 3))

    def test_single_element_case(self):
        self.assertEqual(union_elements((1,), (2,)), (1, 2))
        self.assertEqual(union_elements(('a',), ('b',)), ('a', 'b'))

    def test_duplicate_elements(self):
        self.assertEqual(union_elements((1, 1, 2), (2, 3)), (1, 2, 3))
        self.assertEqual(union_elements(('a', 'a', 'b'), ('b', 'c')), ('a', 'b', 'c'))

    def test_negative_numbers(self):
        self.assertEqual(union_elements((-1, 2, -3), (4, -5, 6)), (-1, 2, -3, 4, -5, 6))
        self.assertEqual(union_elements(('a', 'b', '-c'), ('d', '-e', 'f')), ('a', 'b', '-c', 'd', '-e', 'f'))
