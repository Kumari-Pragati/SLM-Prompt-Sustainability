import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(new_tuple([1, 2, 3], "test"), (1, 2, 3, "test"))

    def test_empty_list(self):
        self.assertEqual(new_tuple([], "empty"), ("empty",))

    def test_empty_string(self):
        self.assertEqual(new_tuple([1, 2, 3], ""), (1, 2, 3, ""))

    def test_single_element_list(self):
        self.assertEqual(new_tuple([4], "single"), (4, "single"))

    def test_large_list(self):
        self.assertEqual(new_tuple(list(range(1, 1001)), "large"), tuple(range(1, 1001)) + ("large",))

    def test_negative_numbers(self):
        self.assertEqual(new_tuple([-1, -2, -3], "negative"), ( -1, -2, -3, "negative"))

    def test_mixed_list(self):
        self.assertEqual(new_tuple([1, "two", 3.0, False], "mixed"), (1, "two", 3.0, False, "mixed"))
