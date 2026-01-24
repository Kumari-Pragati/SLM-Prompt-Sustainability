import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    
    def test_typical_inputs(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(5), 131)
        
    def test_boundary_conditions(self):
        self.assertEqual(jacobsthal_lucas(2), 5)
        self.assertEqual(jacobsthal_lucas(3), 11)
        
    def test_edge_cases(self):
        self.assertEqual(jacobsthal_lucas(4), 23)
        self.assertEqual(jacobsthal_lucas(6), 379)
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas('a')
        with self.assertRaises(ValueError):
            jacobsthal_lucas(-1)
