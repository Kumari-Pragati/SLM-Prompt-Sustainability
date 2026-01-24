import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_set((1,)), {1})

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_to_set((1, 2, 3)), {1, 2, 3})

    def test_tuple_with_duplicates(self):
        self.assertEqual(tuple_to_set((1, 1, 2, 2, 3)), {1, 2, 3})

    def test_tuple_with_negative_numbers(self):
        self.assertEqual(tuple_to_set((-1, -2, -3)), {-1, -2, -3})

    def test_tuple_with_zero(self):
        self.assertEqual(tuple_to_set((0,)), {0})

    def test_tuple_with_mixed_types(self):
        self.assertEqual(tuple_to_set((1, 'a', 2.5)), {1, 'a', 2.5})

    def test_tuple_with_empty_string(self):
        self.assertEqual(tuple_to_set(('a', '', 'c')), {'a', '', 'c'})
