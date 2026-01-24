import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_empty_string(self):
        """Test swapping count for an empty string"""
        self.assertEqual(swap_count(''), 0)

    def test_single_bracket(self):
        """Test swapping count for a single bracket"""
        self.assertEqual(swap_count('['), 0)
        self.assertEqual(swap_count(']'), 0)

    def test_simple_brackets(self):
        """Test swapping count for simple bracket pairs"""
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('()'), 0)
        self.assertEqual(swap_count('{}'), 0)

    def test_mixed_brackets(self):
        """Test swapping count for mixed bracket pairs"""
        self.assertEqual(swap_count('[](){}'), 0)

    def test_imbalanced_brackets_left(self):
        """Test swapping count for imbalanced brackets with extra left brackets"""
        self.assertEqual(swap_count('([{', 3)
        self.assertEqual(swap_count('([{[]}', 3)

    def test_imbalanced_brackets_right(self):
        """Test swapping count for imbalanced brackets with extra right brackets"""
        self.assertEqual(swap_count(']])}', 3)
        self.assertEqual(swap_count(']][{]}', 3)

    def test_invalid_characters(self):
        """Test swapping count for strings containing invalid characters"""
        self.assertEqual(swap_count('[a]'), 0)
        self.assertEqual(swap_count('[z]'), 0)
        self.assertEqual(swap_count('{!}'), 0)
        self.assertEqual(swap_count('(#)'), 0)
