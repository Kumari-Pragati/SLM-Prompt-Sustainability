import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 2), 
                         [('red', 'red'), ('red', 'green'), ('red', 'blue'), 
                          ('green', 'green'), ('green', 'blue'), 
                          ('blue', 'blue')])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 0), [()])

    def test_edge_case_l_equals_empty(self):
        self.assertEqual(combinations_colors([], 2), [])

    def test_boundary_case_n_equals_length_of_l(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 3), 
                         [('red', 'red', 'red'), ('red', 'red', 'green'), 
                          ('red', 'red', 'blue'), ('red', 'green', 'green'), 
                          ('red', 'green', 'blue'), ('red', 'blue', 'blue'), 
                          ('green', 'green', 'green'), 
                          ('green', 'green', 'blue'), 
                          ('green', 'blue', 'blue'), 
                          ('blue', 'blue', 'blue')])

    def test_corner_case_duplicates_in_l(self):
        self.assertEqual(combinations_colors(['red', 'red', 'blue'], 2), 
                         [('red', 'red'), ('red', 'red'), ('red', 'blue'), 
                          ('red', 'blue'), ('red', 'blue'), 
                          ('red', 'blue'), ('blue', 'blue')])
