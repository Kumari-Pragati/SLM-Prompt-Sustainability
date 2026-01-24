import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_new_tuple_with_empty_list(self):
        self.assertEqual(new_tuple([], "test_str"), ("test_str",))

    def test_new_tuple_with_single_element_list(self):
        self.assertEqual(new_tuple([1], "test_str"), (1, "test_str"))

    def test_new_tuple_with_multiple_elements_list(self):
        self.assertEqual(new_tuple([1, 2, 3], "test_str"), (1, 2, 3, "test_str"))

    def test_new_tuple_with_string_list(self):
        self.assertEqual(new_tuple(["test", "str"], "test_str"), ("test", "str", "test_str"))
