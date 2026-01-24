import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(remove_Occ('hello', 'l'), 'heo')

    # Test for edge and boundary conditions
    def test_empty_input(self):
        self.assertEqual(remove_Occ('', 'a'), '')

    def test_char_not_in_string(self):
        self.assertEqual(remove_Occ('hello', 'z'), 'hello')

    def test_string_with_one_char(self):
        self.assertEqual(remove_Occ('a', 'a'), '')

    # Test for more complex or corner cases
    def test_string_with_multiple_chars(self):
        self.assertEqual(remove_Occ('aabbcc', 'b'), 'aac')

    def test_string_with_repeated_chars(self):
        self.assertEqual(remove_Occ('aabbcc', 'a'), 'bbc')

    def test_string_with_same_char_multiple_times(self):
        self.assertEqual(remove_Occ('aabbaabb', 'a'), 'bb')
