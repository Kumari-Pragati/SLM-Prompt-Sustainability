import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_single_swap(self):
        self.assertEqual(min_Swaps('abc', 'abd'), 1)

    def test_multiple_swaps(self):
        self.assertEqual(min_Swaps('abc', 'abdcd'), 2)

    def test_not_possible(self):
        self.assertEqual(min_Swaps('abc', 'def'), 'Not Possible')

    def test_single_character_left(self):
        self.assertEqual(min_Swaps('abc', 'ab'), 'Not Possible')

    def test_single_character_right(self):
        self.assertEqual(min_Swaps('abc', 'abcd'), 'Not Possible')

    def test_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_one_empty_string(self):
        self.assertEqual(min_Swaps('abc', ''), 'Not Possible')

    def test_two_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 'Not Possible')
