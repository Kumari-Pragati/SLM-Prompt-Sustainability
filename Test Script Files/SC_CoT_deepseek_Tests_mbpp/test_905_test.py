import unittest

from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sum_of_square(3), 14)
        
    def test_boundary_case(self):
        self.assertEqual(sum_of_square(0), 1)
        
    def test_edge_case(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        
    def test_special_case(self):
        self.assertEqual(sum_of_square(5), 153)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_of_square("3")
        with self.assertRaises(ValueError):
            sum_of_square(-3)
