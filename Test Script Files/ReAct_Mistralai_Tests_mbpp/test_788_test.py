import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(new_tuple([], "test_str"), ("test_str",))

    def test_single_element_list(self):
        self.assertEqual(new_tuple([1], "test_str"), (1, "test_str"))

    def test_multiple_elements_list(self):
        self.assertEqual(new_tuple([1, 2, 3], "test_str"), (1, 2, 3, "test_str"))

    def test_negative_list_element(self):
        self.assertEqual(new_tuple([-1, 0, 1], "test_str"), (-1, 0, 1, "test_str"))

    def test_empty_string(self):
        self.assertEqual(new_tuple([1, 2, 3], ""), (1, 2, 3))

    def test_whitespace_string(self):
        self.assertEqual(new_tuple([1, 2, 3], "   "), (1, 2, 3, "   "))

    def test_long_string(self):
        long_string = "a" * 100
        self.assertEqual(new_tuple([1, 2, 3], long_string), (1, 2, 3, long_string))

    def test_non_string_type(self):
        with self.assertRaises(TypeError):
            new_tuple([1, 2, 3], 123)
