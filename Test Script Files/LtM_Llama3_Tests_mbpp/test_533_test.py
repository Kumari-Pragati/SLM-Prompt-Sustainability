import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_datatype((1, 2, 3), int), [1, 2, 3])
        self.assertEqual(remove_datatype(("a", "b", "c"), str), ["a", "b", "c"])
        self.assertEqual(remove_datatype([1, 2, 3], int), [1, 2, 3])
        self.assertEqual(remove_datatype(["a", "b", "c"], str), ["a", "b", "c"])

    def test_empty_input(self):
        self.assertEqual(remove_datatype((), int), [])
        self.assertEqual(remove_datatype((), str), [])

    def test_non_existent_type(self):
        self.assertEqual(remove_datatype([1, 2, 3], object), [1, 2, 3])
        self.assertEqual(remove_datatype(["a", "b", "c"], object), ["a", "b", "c"])

    def test_mixed_types(self):
        self.assertEqual(remove_datatype([1, "a", 3.0], int), [1, 3])
        self.assertEqual(remove_datatype(["a", "b", "c"], str), ["a", "b", "c"])
        self.assertEqual(remove_datatype([1, "a", 3.0], str), ["a"])
        self.assertEqual(remove_datatype([1, "a", 3.0], float), [3.0])
