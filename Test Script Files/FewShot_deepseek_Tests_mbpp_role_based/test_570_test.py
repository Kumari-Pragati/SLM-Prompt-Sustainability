import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = ["hello world", "python is fun"]
        charlist = ["world"]
        expected_output = ["hello  ", "python is fun"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_edge_case_empty_list(self):
        list1 = []
        charlist = ["world"]
        expected_output = []
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_boundary_case_single_word(self):
        list1 = ["hello"]
        charlist = ["hello"]
        expected_output = []
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_boundary_case_all_words_to_remove(self):
        list1 = ["hello world", "python is fun"]
        charlist = ["hello", "world", "python", "is", "fun"]
        expected_output = [""]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_invalid_input_type(self):
        list1 = ["hello world", "python is fun"]
        charlist = ["world"]
        with self.assertRaises(TypeError):
            remove_words(list1, 123)
