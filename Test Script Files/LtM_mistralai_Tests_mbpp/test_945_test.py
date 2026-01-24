import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertIsInstance(tuple_to_set((1, 2, 3)), set)
        self.assertEqual(tuple_to_set((1, 2, 3)), {1, 2, 3})

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_to_set(()), set)
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element_tuple(self):
        self.assertIsInstance(tuple_to_set((1,)), set)
        self.assertEqual(tuple_to_set((1,)), {1})

    def test_mixed_types(self):
        self.assertRaises(TypeError, tuple_to_set, (1, 'a', 3.14))

    def test_duplicate_elements(self):
        self.assertIsInstance(tuple_to_set((1, 1, 2, 3)), set)
        self.assertEqual(tuple_to_set((1, 1, 2, 3)), {1, 2, 3})
