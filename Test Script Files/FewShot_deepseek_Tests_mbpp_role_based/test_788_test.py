import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [1, 2, 3]
        test_str = "test"
        expected_result = ((1, 2, 3), "test")
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_empty_list(self):
        test_list = []
        test_str = "test"
        expected_result = (("test",),)
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_single_element_list(self):
        test_list = [1]
        test_str = "test"
        expected_result = ((1,), "test")
        self.assertEqual(new_tuple(test_list, test_str), expected_result)

    def test_error_handling(self):
        test_list = [1, 2, 3]
        test_str = 123  # Invalid input, should be a string
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)
