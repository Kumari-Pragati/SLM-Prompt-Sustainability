import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 24)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 32)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3)), 40)

    def test_tuple_with_mixed_types(self):
        self.assertEqual(tuple_size((1, 'a', 3.14)), 56)

    def test_tuple_with_large_elements(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 72)

    def test_tuple_with_nested_tuples(self):
        self.assertEqual(tuple_size(((1, 2), 3, 4)), 80)

    def test_tuple_with_large_elements_and_nested_tuples(self):
        self.assertEqual(tuple_size(((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 11, 12)), 96)
