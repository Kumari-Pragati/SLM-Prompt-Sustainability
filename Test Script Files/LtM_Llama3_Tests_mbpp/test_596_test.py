import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 48)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 56)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3)), 64)

    def test_tuple_with_mixed_types(self):
        self.assertEqual(tuple_size((1, 'a', 3.14)), 72)

    def test_tuple_with_large_elements(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 80)

    def test_tuple_with_large_elements_and_mixed_types(self):
        self.assertEqual(tuple_size((1, 'a', 3.14, 2, 4, 5, 6, 7, 8, 9, 10)), 96)

    def test_tuple_with_repeated_elements(self):
        self.assertEqual(tuple_size((1, 1, 1, 1, 1, 1, 1, 1, 1, 1)), 80)

    def test_tuple_with_repeated_elements_and_mixed_types(self):
        self.assertEqual(tuple_size((1, 'a', 3.14, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10)), 112)
