import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a test string with long words like supercalifragilisticexpialidocious"
        self.assertEqual(find_long_word(text), ['supercalifragilisticexpialidocious'])

    def test_no_long_word(self):
        text = "This is a test string with short words"
        self.assertEqual(find_long_word(text), [])

    def test_edge_case_single_long_word(self):
        text = "supercalifragilisticexpialidocious"
        self.assertEqual(find_long_word(text), ['supercalifragilisticexpialidocious'])

    def test_edge_case_multiple_long_words(self):
        text = "supercalifragilisticexpialidocious and anotherlongword"
        self.assertEqual(find_long_word(text), ['supercalifragilisticexpialidocious', 'anotherlongword'])

    def test_edge_case_special_characters(self):
        text = "This string contains special characters @#$%^&*()"
        self.assertEqual(find_long_word(text), [])

    def test_edge_case_numbers(self):
        text = "This string contains numbers 1234567890"
        self.assertEqual(find_long_word(text), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_long_word(12345)
