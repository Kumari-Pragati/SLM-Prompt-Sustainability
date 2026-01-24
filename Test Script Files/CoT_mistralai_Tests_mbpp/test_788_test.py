import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_empty_list_and_str(self):
        self.assertEqual(new_tuple([], "test"), ("test",))

    def test_list_and_empty_str(self):
        self.assertEqual(new_tuple(["a", "b"], ""), ("a", "b))

    def test_list_and_str(self):
        self.assertEqual(new_tuple(["a", "b"], "test"), ("a", "b", "test"))

    def test_list_with_duplicates_and_str(self):
        self.assertEqual(new_tuple(["a", "b", "a"], "test"), ("a", "b", "a", "test"))

    def test_str_and_list(self):
        self.assertEqual(new_tuple("test", ["a", "b"]), ("test", "a", "b"))

    def test_list_with_only_str_and_str(self):
        self.assertEqual(new_tuple(["test"], "test"), ("test", "test"))

    def test_list_with_int_and_str(self):
        with self.assertRaises(TypeError):
            new_tuple([1, "test"])

    def test_str_with_int_and_list(self):
        with self.assertRaises(TypeError):
            new_tuple("test", [1])

    def test_list_with_list_and_str(self):
        with self.assertRaises(TypeError):
            new_tuple([[1], "test"])

    def test_str_with_str_and_list(self):
        with self.assertRaises(TypeError):
            new_tuple("test", ["test", "list"])
