import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_empty_union(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_element_union(self):
        self.assertEqual(union_elements((1,), (2,)), (1, 2))
        self.assertEqual(union_elements((2,), (1,)), (1, 2))

    def test_multiple_elements_union(self):
        self.assertEqual(union_elements((1, 2, 3), (2, 4, 3)), (1, 2, 4))
        self.assertEqual(union_elements((2, 4, 3), (1, 2, 3)), (1, 2, 4))

    def test_same_elements_union(self):
        self.assertEqual(union_elements((1, 1, 2), (2, 1)), (1, 2))

    def test_duplicate_elements_union(self):
        self.assertEqual(union_elements((1, 1, 2), (2, 1, 3)), (1, 2, 3))

    def test_negative_numbers_union(self):
        self.assertEqual(union_elements((-1, 0, 1), (-2, -1, 0, 1)), (-2, -1, 0, 1))

    def test_empty_tuple_input(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), ())

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), [1, 2, 3])
