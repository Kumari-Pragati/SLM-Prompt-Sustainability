import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 2), 
                         [('red', 'red'), ('red', 'green'), ('red', 'blue'), 
                          ('green', 'green'), ('green', 'blue'), 
                          ('blue', 'blue')])

    def test_single_color(self):
        self.assertEqual(combinations_colors(['red'], 2), [('red', 'red')])

    def test_empty_list(self):
        self.assertEqual(combinations_colors([], 2), [])

    def test_large_n(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 5), 
                         [('red', 'red', 'red', 'red', 'red'), 
                          ('red', 'red', 'red', 'red', 'green'), 
                          ('red', 'red', 'red', 'red', 'blue'), 
                          ('red', 'red', 'red', 'green', 'green'), 
                          ('red', 'red', 'red', 'green', 'blue'), 
                          ('red', 'red', 'red', 'blue', 'blue'), 
                          ('red', 'red', 'green', 'green', 'green'), 
                          ('red', 'red', 'green', 'green', 'blue'), 
                          ('red', 'red', 'green', 'blue', 'blue'), 
                          ('red', 'red', 'blue', 'blue', 'blue'), 
                          ('red', 'green', 'green', 'green', 'green'), 
                          ('red', 'green', 'green', 'green', 'blue'), 
                          ('red', 'green', 'green', 'blue', 'blue'), 
                          ('red', 'green', 'blue', 'blue', 'blue'), 
                          ('red', 'blue', 'blue', 'blue', 'blue'), 
                          ('green', 'green', 'green', 'green', 'green'), 
                          ('green', 'green', 'green', 'green', 'blue'), 
                          ('green', 'green', 'green', 'blue', 'blue'), 
                          ('green', 'green', 'blue', 'blue', 'blue'), 
                          ('green', 'blue', 'blue', 'blue', 'blue'), 
                          ('blue', 'blue', 'blue', 'blue', 'blue')])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            combinations_colors(['red', 'green', 'blue'], -1)
