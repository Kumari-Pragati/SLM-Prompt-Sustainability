import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(swap_count('[]'), 0)

    def test_imbalance(self):
        self.assertEqual(swap_count('[[[]]]'), 2)

    def test_multiple_imbalances(self):
        self.assertEqual(swap_count('[[[]]][][]'), 4)

    def test_empty_string(self):
        self.assertEqual(swap_count(''), 0)

    def test_single_character(self):
        self.assertEqual(swap_count('['), 0)

    def test_multiple_characters(self):
        self.assertEqual(swap_count('[]'), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            swap_count(123)
