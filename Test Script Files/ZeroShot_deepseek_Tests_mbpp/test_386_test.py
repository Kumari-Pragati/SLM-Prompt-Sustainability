import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(swap_count(''), 0)

    def test_balanced_string(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('[[]]'), 0)
        self.assertEqual(swap_count('[[[]]]'), 0)

    def test_unbalanced_string(self):
        self.assertEqual(swap_count('[['), 1)
        self.assertEqual(swap_count('[[['), 2)
        self.assertEqual(swap_count('[[[['), 3)

    def test_mixed_string(self):
        self.assertEqual(swap_count('[[][]]'), 0)
        self.assertEqual(swap_count('[[][[]]'), 1)
        self.assertEqual(swap_count('[[][[]]'), 1)
        self.assertEqual(swap_count('[[][][]]'), 0)
