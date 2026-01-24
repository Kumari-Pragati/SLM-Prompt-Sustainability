import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = ["apple", "banana", "cherry"]
        self.assertEqual(len_log(list1), 5)

    def test_edge_case_empty_list(self):
        list1 = []
        self.assertEqual(len_log(list1), 0)

    def test_edge_case_single_element_list(self):
        list1 = ["hello"]
        self.assertEqual(len_log(list1), 5)

    def test_edge_case_multiple_element_list(self):
        list1 = ["apple", "banana", "cherry", "date", "elderberry"]
        self.assertEqual(len_log(list1), 7)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            len_log("hello")
