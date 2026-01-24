import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_normal_input(self):
        self.assertIsInstance(tuple_to_set((1, 2, 3)), set)
        self.assertSetEqual(set([1, 2, 3]), tuple_to_set((1, 2, 3)))

    def test_empty_input(self):
        self.assertIsInstance(tuple_to_set(()), set)
        self.assertSetEqual(set(), tuple_to_set(()))

    def test_single_element_input(self):
        self.assertIsInstance(tuple_to_set((1,)), set)
        self.assertSetEqual(set([1]), tuple_to_set((1,)))

    def test_mixed_types_input(self):
        self.assertRaises(TypeError, tuple_to_set, (1, 'a', 3))

    def test_duplicate_elements_input(self):
        self.assertSetEqual(set([1, 2, 2, 3]), tuple_to_set((1, 2, 2, 3)))

    def test_negative_numbers_input(self):
        self.assertSetEqual(set([-1, 0, 1]), tuple_to_set((-1, 0, 1)))

    def test_large_numbers_input(self):
        self.assertSetEqual(set(range(1000)), tuple_to_set(tuple(range(1000))))
