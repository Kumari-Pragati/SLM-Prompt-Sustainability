import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(list_tuple([]), ())

    def test_single_element_list(self):
        self.assertEqual(list_tuple([42]), (42,))

    def test_large_list(self):
        self.assertEqual(list_tuple(list(range(1000))), tuple(range(1000)))

    def test_string_list(self):
        self.assertEqual(list_tuple(["apple", "banana", "cherry"]), ("apple", "banana", "cherry"))

    def test_mixed_type_list(self):
        with self.assertRaises(TypeError):
            list_tuple([1, "two", 3.0])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            list_tuple("not a list")
