import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(find_Divisor(10, 10), 10)
        self.assertEqual(find_Divisor(20, 15), 2)
    
    def test_edge_cases(self):
        self.assertEqual(find_Divisor(0, 0), 0)
        self.assertEqual(find_Divisor(0, 10), 2)
        self.assertEqual(find_Divisor(10, 0), 2)
    
    def test_boundary_cases(self):
        self.assertEqual(find_Divisor(1, 1), 1)
        self.assertEqual(find_Divisor(2, 2), 2)
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Divisor("10", 10)
        with self.assertRaises(TypeError):
            find_Divisor(10, "10")
        with self.assertRaises(TypeError):
            find_Divisor("10", "10")
