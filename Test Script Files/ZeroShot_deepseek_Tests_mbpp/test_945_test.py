import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_set((1,)), {1})

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_to_set((1, 2, 2, 3, 4, 4, 4, 5)), {1, 2, 3, 4, 5})

    def test_duplicate_elements_tuple(self):
        self.assertEqual(tuple_to_set((1, 1, 1, 2, 2, 3)), {1, 2, 3})

    def test_string_tuple(self):
        self.assertEqual(tuple_to_set(('a', 'b', 'b', 'c')), {'a', 'b', 'c'})

    def test_mixed_type_tuple(self):
        self.assertEqual(tuple_to_set((1, 'a', 2, 'b')), {1, 'a', 2, 'b'})
