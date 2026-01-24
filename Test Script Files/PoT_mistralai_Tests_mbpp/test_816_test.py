import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(clear_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(clear_tuple((1,)), ())

    def test_multiple_elements_tuple(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())

    def test_tuple_with_none(self):
        self.assertEqual(clear_tuple((1, None, 3)), (1, 3))

    def test_tuple_with_lists(self):
        self.assertEqual(clear_tuple(((1,), [2, 3]))), ())

    def test_tuple_with_empty_list(self):
        self.assertEqual(clear_tuple((1, [], 3)), (1, 3))

    def test_tuple_with_nested_tuples(self):
        self.assertEqual(clear_tuple((1, (2, 3), 4)), (1, (2, 3), 4))
