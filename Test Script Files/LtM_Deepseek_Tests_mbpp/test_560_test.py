import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_simple_union(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))

    def test_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(union_elements((1,), (1,)), (1,))
        self.assertEqual(union_elements((1,), (2,)), (1, 2))

    def test_duplicate_elements(self):
        self.assertEqual(union_elements((1, 2, 2, 3), (2, 3, 4, 4)), (1, 2, 3, 4))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 1001))
        self.assertEqual(union_elements(large_tuple, large_tuple), large_tuple)
