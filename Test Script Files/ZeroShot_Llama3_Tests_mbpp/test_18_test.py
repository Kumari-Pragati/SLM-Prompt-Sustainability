import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_remove_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "World"), "Hello, ")
        self.assertEqual(remove_dirty_chars("Hello, World!", "Hello"), " World!")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,"), "Hello, ")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello"), "")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello,World"), "")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello,World,World"), "")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello,World,World,World"), "")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello,World,World,World,World"), "")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello,World,World,World,World,World"), "")
        self.assertEqual(remove_dirty_chars("Hello, World!", "World,Hello,World,World,World,World,World,World"), "")

    def test_remove_dirty_chars_empty_string(self):
        self.assertEqual(remove_dirty_chars("", ""), "")

    def test_remove_dirty_chars_single_char(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "")
        self.assertEqual(remove_dirty_chars("a", "b"), "a")
        self.assertEqual(remove_dirty_chars("a", "c"), "a")
        self.assertEqual(remove_dirty_chars("a", "a"), "")

    def test_remove_dirty_chars_multiple_chars(self):
        self.assertEqual(remove_dirty_chars("abc", "abc"), "")
        self.assertEqual(remove_dirty_chars("abc", "ab"), "c")
        self.assertEqual(remove_dirty_chars("abc", "ac"), "b")
        self.assertEqual(remove_dirty_chars("abc", "bc"), "a")
        self.assertEqual(remove_dirty_chars("abc", "abc,abc"), "")
