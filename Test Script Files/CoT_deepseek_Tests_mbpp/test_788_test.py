import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [1, 2, 3]
        test_str = "test"
        expected_output = ((1, 2, 3, "test"))
        self.assertEqual(new_tuple(test_list, test_str), expected_output)

    def test_empty_list(self):
        test_list = []
        test_str = "test"
        expected_output = (("test",))
        self.assertEqual(new_tuple(test_list, test_str), expected_output)

    def test_single_element_list(self):
        test_list = [1]
        test_str = "test"
        expected_output = ((1, "test"),)
        self.assertEqual(new_tuple(test_list, test_str), expected_output)

    def test_long_string(self):
        test_list = [1, 2, 3]
        test_str = "a" * 1000
        expected_output = ((1, 2, 3, "a" * 1000),)
        self.assertEqual(new_tuple(test_list, test_str), expected_output)

    def test_empty_string(self):
        test_list = [1, 2, 3]
        test_str = ""
        expected_output = ((1, 2, 3, ""),)
        self.assertEqual(new_tuple(test_list, test_str), expected_output)

    def test_invalid_input_type(self):
        test_list = [1, 2, 3]
        test_str = 123
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)
