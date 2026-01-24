import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(tuple_to_set((1, 2, 3)), ({1, 2, 3},))

    def test_empty_input(self):
        self.assertEqual(tuple_to_set(()), ({},))

    def test_single_element_input(self):
        self.assertEqual(tuple_to_set((4,)), ({4},))

    def test_duplicates_in_input(self):
        self.assertEqual(tuple_to_set((1, 2, 2, 3)), ({1, 2, 3},))

    def test_non_hashable_input(self):
        with self.assertRaises(TypeError):
            tuple_to_set([1, 2, 3])

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            tuple_to_set("hello")

    def test_mixed_type_input(self):
        with self.assertRaises(TypeError):
            tuple_to_set((1, "hello", 3.0))
