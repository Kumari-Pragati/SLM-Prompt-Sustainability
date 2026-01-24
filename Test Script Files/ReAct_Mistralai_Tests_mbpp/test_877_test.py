import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_sort_alphabetical(self):
        """Test sorting a string alphabetically."""
        self.assertEqual(sort_String('abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')

    def test_sort_mixed_case(self):
        """Test sorting a string with mixed case."""
        self.assertEqual(sort_String('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'AbCdefghijklmnopqrstuvwxyz')

    def test_sort_special_characters(self):
        """Test sorting a string with special characters."""
        self.assertEqual(sort_String('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,./')

    def test_sort_numbers(self):
        """Test sorting a string with numbers."""
        self.assertEqual(sort_String('0123456789'), '0123456789')

    def test_sort_mixed_numbers(self):
        """Test sorting a string with mixed numbers."""
        self.assertEqual(sort_String('0a1b2c3d4e5f6g7h8i9'), '0123456789abcdefghi')

    def test_sort_empty_string(self):
        """Test sorting an empty string."""
        self.assertEqual(sort_String(''), '')

    def test_sort_single_character(self):
        """Test sorting a single character."""
        self.assertEqual(sort_String('a'), 'a')

    def test_sort_long_string(self):
        """Test sorting a long string."""
        long_string = ''.join(chr(i) for i in range(1000))
        self.assertEqual(sort_String(long_string), long_string)

    def test_sort_string_with_duplicates(self):
        """Test sorting a string with duplicates."""
        self.assertEqual(sort_String('aaabbbccc'), 'aaabbbccc')

    def test_sort_string_with_whitespace(self):
        """Test sorting a string with whitespace."""
        self.assertEqual(sort_String('hello world'), 'hello world')

    def test_sort_string_with_leading_trailing_whitespace(self):
        """Test sorting a string with leading and trailing whitespace."""
        self.assertEqual(sort_String('   hello world   '), 'hello world')
