import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertTupleEqual(clear_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertTupleEqual(clear_tuple((1,)), ())

    def test_multiple_elements_tuple(self):
        self.assertTupleEqual(clear_tuple((1, 2, 3)), ())

    def test_immutable_tuple(self):
        self.assertTupleEqual(clear_tuple((tuple([1, 2, 3]),)), ())

    def test_mixed_types_tuple(self):
        self.assertTupleEqual(clear_tuple((1, "str", (1, 2, 3))), ())

    def test_none_type_tuple(self):
        self.assertRaises(TypeError, clear_tuple, (None,))

    def test_list_type_tuple(self):
        self.assertRaises(TypeError, clear_tuple, ((list([1, 2, 3]),)))
