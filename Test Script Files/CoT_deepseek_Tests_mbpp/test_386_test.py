import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('[[]]'), 0)
        self.assertEqual(swap_count('[[[]]]'), 0)
        self.assertEqual(swap_count('[[][][]]'), 0)

    def test_imbalance_case(self):
        self.assertEqual(swap_count('[)('), 1)
        self.assertEqual(swap_count('[(])'), 1)
        self.assertEqual(swap_count('[[)]]'), 1)
        self.assertEqual(swap_count('[()][]'), 0)

    def test_empty_string(self):
        self.assertEqual(swap_count(''), 0)

    def test_single_bracket(self):
        self.assertEqual(swap_count('['), 0)
        self.assertEqual(swap_count(']'), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            swap_count(123)
        with self.assertRaises(TypeError):
            swap_count(None)
        with self.assertRaises(TypeError):
            swap_count(['[', ']'])
