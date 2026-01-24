import unittest
from mbpp_255_code import combinations_with_replacement
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 2), 
                         list(combinations_with_replacement(['red', 'green', 'blue'], 2)))
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 3), 
                         list(combinations_with_replacement(['red', 'green', 'blue'], 3)))
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 1), 
                         list(combinations_with_replacement(['red', 'green', 'blue'], 1)))
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 0), 
                         list(combinations_with_replacement(['red', 'green', 'blue'], 0)))
        self.assertEqual(combinations_colors([], 2), 
                         list(combinations_with_replacement([], 2)))
