import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 2), 
                         [('red', 'red'), ('green', 'green'), ('blue', 'blue'), 
                          ('red', 'green'), ('green', 'red'), ('red', 'blue'), 
                          ('blue', 'red'), ('green', 'blue'), ('blue', 'green')])

    def test_edge_conditions(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 0), [()])
        self.assertEqual(combinations_colors([], 3), [])

    def test_complex_cases(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 3), 
                         [('red', 'red', 'red'), ('green', 'green', 'green'), 
                          ('blue', 'blue', 'blue'), ('red', 'red', 'green'), 
                          ('red', 'green', 'red'), ('green', 'red', 'red'), 
                          ('red', 'red', 'blue'), ('red', 'blue', 'red'), 
                          ('blue', 'red', 'red'), ('red', 'green', 'blue'), 
                          ('green', 'blue', 'red'), ('blue', 'green', 'red'), 
                          ('red', 'blue', 'green'), ('blue', 'red', 'green'), 
                          ('green', 'red', 'blue'), ('red', 'green', 'green'), 
                          ('green', 'green', 'red'), ('green', 'blue', 'blue'), 
                          ('blue', 'blue', 'green'), ('blue', 'green', 'blue'), 
                          ('green', 'green', 'blue'), ('green', 'blue', 'green')])
