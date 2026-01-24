import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Max_Len_Even("This is a test string"), "is")

    def test_edge_case(self):
        self.assertEqual(find_Max_Len_Even(" "), "-1")

    def test_boundary_case(self):
        self.assertEqual(find_Max_Len_Even("a"), "-1")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Max_Len_Even(123)

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_string_with_even_length_word(self):
        self.assertEqual(find_Max_Len_Even("This is a test string with even length word"), "even")
