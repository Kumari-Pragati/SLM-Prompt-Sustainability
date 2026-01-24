import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('[[]]'), 0)
        self.assertEqual(swap_count('[[[]]]'), 0)
        self.assertEqual(swap_count('[[][][]]'), 0)

    def test_single_bracket_case(self):
        self.assertEqual(swap_count('['), 0)
        self.assertEqual(swap_count(']'), 0)

    def test_imbalance_case(self):
        self.assertEqual(swap_count('[]['), 1)
        self.assertEqual(swap_count('[]]['), 1)
        self.assertEqual(swap_count('[[]]['), 1)
        self.assertEqual(swap_count('[[[]]][], 1)

    def test_empty_string_case(self):
        self.assertEqual(swap_count(''), 0)

    def test_large_input_case(self):
        self.assertEqual(swap_count('[' * 10000 + ']' * 10000), 0)
