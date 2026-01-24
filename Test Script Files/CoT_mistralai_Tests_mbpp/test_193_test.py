import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertTupleEqual(remove_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertTupleEqual(remove_tuple((1,)), (1,))

    def test_multiple_elements_tuple(self):
        self.assertTupleEqual(remove_tuple((1, 2, 3, 2, 1)), (1, 2, 3))

    def test_duplicate_elements_tuple(self):
        self.assertTupleEqual(remove_tuple((1, 2, 2, 3, 2, 1)), (1, 2, 3))

    def test_mixed_types_tuple(self):
        self.assertRaises(TypeError, remove_tuple, (1, 'a', 2.5))

    def test_tuple_with_none(self):
        self.assertTupleEqual(remove_tuple((None, 1, 2)), (1, 2))

    def test_tuple_with_list(self):
        self.assertRaises(TypeError, remove_tuple, ([1], 2))
