import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [1, 2, 3]
        test_str = "four"
        expected_result = (1, 2, 3, "four")
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_empty_list(self):
        test_list = []
        test_str = "empty"
        expected_result = ("empty",)
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_single_element_list(self):
        test_list = [5]
        test_str = "five"
        expected_result = (5, "five")
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_large_list(self):
        test_list = list(range(1, 1001))
        test_str = "large"
        expected_result = tuple(test_list + ["large"])
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_empty_string(self):
        test_list = [1, 2, 3]
        test_str = ""
        expected_result = (1, 2, 3)
        self.assertEqual(new_tuple(test_list, test_str), expected_result)
