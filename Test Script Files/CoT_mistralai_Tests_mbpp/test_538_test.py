import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsInstance(string_list_to_tuple([]), tuple)
        self.assertEqual(string_list_to_tuple([]), ())

    def test_single_element(self):
        self.assertIsInstance(string_list_to_tuple(["a"]), tuple)
        self.assertEqual(string_list_to_tuple(["a"]), ("a",))

    def test_multiple_elements(self):
        self.assertIsInstance(string_list_to_tuple(["a", "b", "c"]), tuple)
        self.assertEqual(string_list_to_tuple(["a", "b", "c"]), ("a", "b", "c"))

    def test_mixed_spaces_and_elements(self):
        self.assertIsInstance(string_list_to_tuple(["a", " ", "b", " ", "c"]), tuple)
        self.assertEqual(string_list_to_tuple(["a", " ", "b", " ", "c"]), ("a", "b", "c"))

    def test_all_spaces(self):
        self.assertIsInstance(string_list_to_tuple([" ", " ", " ", " ", " "]), tuple)
        self.assertEqual(string_list_to_tuple([" ", " ", " ", " ", " "]), ())

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            string_list_to_tuple(123)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            string_list_to_tuple(None)
