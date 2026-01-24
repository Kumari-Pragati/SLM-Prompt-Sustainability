import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertEqual(tuple_to_set((1, 2, 3)), {1, 2, 3})

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_set(()), set())

    def test_duplicate_elements(self):
        self.assertEqual(tuple_to_set((1, 2, 2, 3)), {1, 2, 3})

    def test_large_tuple(self):
        self.assertEqual(tuple_to_set(tuple(range(1, 1001))), set(range(1, 1001)))

    def test_negative_numbers(self):
        self.assertEqual(tuple_to_set((-1, -2, -3)), {-1, -2, -3})

    def test_mixed_types(self):
        self.assertEqual(tuple_to_set((1, 'a', 2.5)), {1, 'a', 2.5})
