import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_to_set(()), set)
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element_tuple(self):
        self.assertIsInstance(tuple_to_set((1,)), set)
        self.assertEqual(tuple_to_set((1,)), {1})

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(tuple_to_set((1, 2, 3)), set)
        self.assertEqual(tuple_to_set((1, 2, 3)), {1, 2, 3})

    def test_duplicate_elements_tuple(self):
        self.assertIsInstance(tuple_to_set((1, 1, 2, 3)), set)
        self.assertEqual(tuple_to_set((1, 1, 2, 3)), {1, 2, 3})

    def test_mixed_types_tuple(self):
        with self.assertRaises(TypeError):
            tuple_to_set((1, 'a', [1]))

    def test_empty_list_as_input(self):
        self.assertIsInstance(tuple_to_set([]), TypeError)

    def test_string_as_input(self):
        self.assertIsInstance(tuple_to_set('abc'), TypeError)
