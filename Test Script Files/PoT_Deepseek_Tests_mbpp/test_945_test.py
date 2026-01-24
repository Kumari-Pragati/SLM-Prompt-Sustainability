import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_to_set((1, 2, 3, 2)), {1, 2, 3})

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_set((5,)), {5})

    def test_duplicate_elements(self):
        self.assertEqual(tuple_to_set((1, 1, 1, 1)), {1})

    def test_large_tuple(self):
        self.assertEqual(tuple_to_set(tuple(range(1000))), set(range(1000)))

    def test_mixed_types(self):
        self.assertEqual(tuple_to_set((1, 'a', 1.0)), {1, 'a', 1.0})

    def test_non_hashable_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_set(([1, 2, 3],))
