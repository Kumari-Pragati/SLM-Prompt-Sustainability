import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_remove_datatype_string(self):
        test_tuple = (1, "hello", 3, "world", 4)
        self.assertListEqual(remove_datatype(test_tuple, str), ["hello", "world"])

    def test_remove_datatype_integer(self):
        test_tuple = (1, "hello", 3, "world", 4)
        self.assertListEqual(remove_datatype(test_tuple, int), [1, 3, 4])

    def test_remove_datatype_list(self):
        test_tuple = ([1, 2, 3], "hello", (1, 2, 3), "world", 4)
        self.assertListEqual(remove_datatype(test_tuple, list), ["hello", "world", 4])

    def test_remove_datatype_tuple(self):
        test_tuple = ([1, 2, 3], "hello", (1, 2, 3), "world", 4)
        self.assertListEqual(remove_datatype(test_tuple, tuple), [1, 2, 3, "hello", "world"])

    def test_remove_datatype_dict(self):
        test_tuple = ({"a": 1, "b": 2}, "hello", (1, 2, 3), "world", 4)
        self.assertListEqual(remove_datatype(test_tuple, dict), ["hello", (1, 2, 3), "world", 4])
