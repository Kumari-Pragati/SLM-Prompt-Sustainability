import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):
    def test_typical_input(self):
        list1 = [1, 2, 3]
        string1 = "Hello {}"
        result = add_string(list1, string1)
        self.assertEqual(result, ["Hello 1", "Hello 2", "Hello 3"])

    def test_edge_case_empty_list(self):
        list2 = []
        string2 = "Hello {}"
        result = add_string(list2, string2)
        self.assertEqual(result, [])

    def test_edge_case_empty_string(self):
        list3 = [1, 2, 3]
        string3 = ""
        result = add_string(list3, string3)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        list4 = [5]
        string4 = "Hello {}"
        result = add_string(list4, string4)
        self.assertEqual(result, ["Hello 5"])

    def test_edge_case_single_element_string(self):
        list5 = [1, 2, 3]
        string5 = "Hello"
        result = add_string(list5, string5)
        self.assertEqual(result, ["Hello", "Hello", "Hello"])

    def test_invalid_input_non_list(self):
        list6 = "not a list"
        string6 = "Hello {}"
        with self.assertRaises(TypeError):
            add_string(list6, string6)

    def test_invalid_input_non_string(self):
        list7 = [1, 2, 3]
        string7 = 123
        with self.assertRaises(TypeError):
            add_string(list7, string7)
