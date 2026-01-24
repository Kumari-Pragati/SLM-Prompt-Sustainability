import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):
    def test_union_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_union_identical_tuples(self):
        self.assertEqual(union_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_union_overlapping_tuples(self):
        self.assertEqual(union_elements((1, 2, 3, 4), (2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_union_non_overlapping_tuples(self):
        self.assertEqual(union_elements((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_union_one_empty_tuple(self):
        self.assertEqual(union_elements((1, 2, 3), ()), (1, 2, 3))

    def test_union_one_single_element_tuple(self):
        self.assertEqual(union_elements((1,), (2, 3)), (1, 2, 3))
