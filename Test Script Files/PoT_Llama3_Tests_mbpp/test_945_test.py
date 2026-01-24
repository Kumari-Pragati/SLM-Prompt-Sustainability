import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(tuple_to_set((1, 2, 3)), {(1, 2, 3)})

    def test_empty(self):
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element(self):
        self.assertEqual(tuple_to_set((1,)), {(1,)})

    def test_duplicates(self):
        self.assertEqual(tuple_to_set((1, 2, 2, 3)), {(1, 2, 3)})

    def test_empty_set(self):
        self.assertEqual(tuple_to_set(set()), set())

    def test_set(self):
        self.assertEqual(tuple_to_set({1, 2, 3}), {(1, 2, 3)})

    def test_tuple_with_duplicates(self):
        self.assertEqual(tuple_to_set((1, 2, 2, 3)), {(1, 2, 3)})

    def test_tuple_with_empty(self):
        self.assertEqual(tuple_to_set(()), set())
