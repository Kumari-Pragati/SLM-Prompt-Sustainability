import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(first_Digit(5), 1)
        self.assertEqual(first_Digit(10), 3)
        self.assertEqual(first_Digit(15), 1)
        self.assertEqual(first_Digit(20), 6)
        
    def test_boundary_conditions(self):
        self.assertEqual(first_Digit(0), 1)
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(2), 2)
        
    def test_edge_cases(self):
        self.assertEqual(first_Digit(3), 6)
        self.assertEqual(first_Digit(4), 4)
        self.assertEqual(first_Digit(6), 2)
        self.assertEqual(first_Digit(7), 8)
        self.assertEqual(first_Digit(8), 4)
        self.assertEqual(first_Digit(9), 1)
        self.assertEqual(first_Digit(10), 3)
        self.assertEqual(first_Digit(11), 0)
        self.assertEqual(first_Digit(12), 6)
        self.assertEqual(first_Digit(13), 2)
        self.assertEqual(first_Digit(14), 4)
        self.assertEqual(first_Digit(15), 1)
        self.assertEqual(first_Digit(16), 8)
        self.assertEqual(first_Digit(17), 2)
        self.assertEqual(first_Digit(18), 4)
        self.assertEqual(first_Digit(19), 6)
        self.assertEqual(first_Digit(20), 6)
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Digit('a')
        with self.assertRaises(ValueError):
            first_Digit(-5)
