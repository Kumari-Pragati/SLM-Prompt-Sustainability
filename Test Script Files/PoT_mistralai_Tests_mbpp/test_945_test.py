import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_typical_case(self):
        self.assertSetEqual(set([1, 2, 3]), tuple_to_set((1, 2, 3)))

    def test_empty_tuple(self):
        self.assertSetEqual(set(), tuple_to_set([]))

    def test_single_element_tuple(self):
        self.assertSetEqual(set([1]), tuple_to_set((1,)))

    def test_duplicate_elements(self):
        self.assertSetEqual(set([1, 1]), tuple_to_set((1, 1, 2)))

    def test_negative_integer(self):
        self.assertSetEqual(set([-1]), tuple_to_set((-1,)))

    def test_float(self):
        self.assertSetEqual(set([3.14]), tuple_to_set((3.14,)))

    def test_string(self):
        self.assertSetEqual(set(["hello"]), tuple_to_set(("hello",)))

    def test_mixed_types(self):
        self.assertSetEqual(set([3, "hello"]), tuple_to_set((3, "hello")))
