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
        self.assertEqual(tuple_to_set((1, 2, 2, 3)), {1, 2, 3})

    def test_tuple_with_non_hashable_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_set((1, [2, 3]))
