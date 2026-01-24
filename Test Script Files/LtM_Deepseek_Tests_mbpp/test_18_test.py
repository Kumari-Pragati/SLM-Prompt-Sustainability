import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(remove_dirty_chars("hello", "aeiou"), "hll")
        self.assertEqual(remove_dirty_chars("world", "dlr"), "wo")

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(remove_dirty_chars("", "aeiou"), "")
        self.assertEqual(remove_dirty_chars("a", "aeiou"), "")
        self.assertEqual(remove_dirty_chars("hello", ""), "hello")

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(remove_dirty_chars("hello world", "dlr"), "heo wor")
        self.assertEqual(remove_dirty_chars("abc", "abc"), "")
        self.assertEqual(remove_dirty_chars("abc", "def"), "abc")
