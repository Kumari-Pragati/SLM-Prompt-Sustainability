import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(swap_count(''), 0)

    def test_single_bracket(self):
        self.assertEqual(swap_count('['), 0)
        self.assertEqual(swap_count(']'), 0)

    def test_simple_brackets(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('()'), 0)
        self.assertEqual(swap_count('{}'), 0)

    def test_balanced_brackets(self):
        self.assertEqual(swap_count('[][]'), 0)
        self.assertEqual(swap_count('()()'), 0)
        self.assertEqual(swap_count('{}{}'), 0)

    def test_unbalanced_brackets(self):
        self.assertEqual(swap_count('[]]'), 1)
        self.assertEqual(swap_count('()]'), 1)
        self.assertEqual(swap_count('{}]'), 1)

    def test_unbalanced_brackets_multiple_swaps(self):
        self.assertEqual(swap_count('[]]]'], 2)
        self.assertEqual(swap_count('()][', 1)
        self.assertEqual(swap_count('{}[', 1)

    def test_invalid_input(self):
        self.assertRaises(ValueError, swap_count, 'a')
        self.assertRaises(ValueError, swap_count, '[]a]')
        self.assertRaises(ValueError, swap_count, 'a[]]')
