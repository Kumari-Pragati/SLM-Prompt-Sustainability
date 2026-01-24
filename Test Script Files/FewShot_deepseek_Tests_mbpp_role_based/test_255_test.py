import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 2), 
                         [('red', 'red'), ('red', 'green'), ('red', 'blue'), 
                          ('green', 'green'), ('green', 'blue'), 
                          ('blue', 'blue')])

    def test_edge_case(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 0), [()])

    def test_boundary_condition(self):
        self.assertEqual(combinations_colors(['red', 'green', 'blue'], 4), 
                         [('red', 'red', 'red', 'red'), 
                          ('red', 'red', 'red', 'green'), 
                          ('red', 'red', 'red', 'blue'), 
                          ('red', 'red', 'green', 'green'), 
                          ('red', 'red', 'green', 'blue'), 
                          ('red', 'red', 'blue', 'blue'), 
                          ('red', 'green', 'green', 'green'), 
                          ('red', 'green', 'green', 'blue'), 
                          ('red', 'green', 'blue', 'blue'), 
                          ('red', 'blue', 'blue', 'blue'), 
                          ('green', 'green', 'green', 'green'), 
                          ('green', 'green', 'green', 'blue'), 
                          ('green', 'green', 'blue', 'blue'), 
                          ('green', 'blue', 'blue', 'blue'), 
                          ('blue', 'blue', 'blue', 'blue')])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            combinations_colors('red', 2)
