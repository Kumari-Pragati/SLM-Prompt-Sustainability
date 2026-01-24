import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['1', '2', '3']))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['1', '2', '3']))

    def test_empty_lists(self):
        self.assertTrue(is_samepatterns([], []))

    def test_same_elements(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'red'], ['1', '1', '1']))

    def test_different_elements(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['1', '2', '2']))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_samepatterns(123, ['1', '2', '3'])
