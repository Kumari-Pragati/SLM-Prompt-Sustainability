import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))

    def test_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(union_elements((1,), (1,)), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(union_elements((1, 2, 2), (2, 3, 3)), (1, 2, 3))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 1001))
        self.assertEqual(union_elements(large_tuple, large_tuple), large_tuple)

    def test_mixed_types(self):
        self.assertEqual(union_elements((1, 'a', True), (1, 'a', False)), (1, 'a', True, False))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), [3, 4, 5])
