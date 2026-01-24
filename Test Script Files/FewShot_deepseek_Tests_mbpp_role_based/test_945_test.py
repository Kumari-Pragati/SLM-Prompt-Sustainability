import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tuple_to_set((1, 2, 3, 4)), {1, 2, 3, 4})

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_set(()), set())

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_set((5,)), {5})

    def test_duplicate_elements(self):
        self.assertEqual(tuple_to_set((1, 2, 2, 3, 3, 4)), {1, 2, 3, 4})

    def test_large_tuple(self):
        self.assertEqual(tuple_to_set(tuple(range(1, 1001))), set(range(1, 1001)))
