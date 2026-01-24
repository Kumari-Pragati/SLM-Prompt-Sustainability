import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_String("hello"), "ehllo")
        self.assertEqual(sort_String("Python"), "hpyotyN")
        self.assertEqual(sort_String("12345"), "12345")

    def test_edge_case_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(sort_String("a"), "a")

    def test_edge_case_uppercase_letters(self):
        self.assertEqual(sort_String("ABC"), "ABC")

    def test_edge_case_mixed_case(self):
        self.assertEqual(sort_String("HeLlO wOrLd"), "eHhLlLlOo wOrRrRrldd")

    def test_corner_case_special_characters(self):
        self.assertEqual(sort_String("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), "!@#$%^&*()_+-=[]{}|;:'\",.<>?/")
