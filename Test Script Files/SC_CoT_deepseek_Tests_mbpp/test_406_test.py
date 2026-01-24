import unittest

from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")
        self.assertEqual(find_Parity(4), "Even Parity")
        self.assertEqual(find_Parity(5), "Odd Parity")
        self.assertEqual(find_Parity(6), "Even Parity")
        self.assertEqual(find_Parity(7), "Odd Parity")
        self.assertEqual(find_Parity(8), "Even Parity")
        self.assertEqual(find_Parity(9), "Odd Parity")
        self.assertEqual(find_Parity(10), "Even Parity")
    
    def test_boundary_conditions(self):
        self.assertEqual(find_Parity(0xFFFFFFFFFFFFFFFF), "Odd Parity")
        self.assertEqual(find_Parity(0xFFFFFFFFFFFFFFFE), "Even Parity")
    
    def test_edge_cases(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")
        self.assertEqual(find_Parity(-2), "Even Parity")
        self.assertEqual(find_Parity(-3), "Odd Parity")
        self.assertEqual(find_Parity(-4), "Even Parity")
        self.assertEqual(find_Parity(-5), "Odd Parity")
        self.assertEqual(find_Parity(-6), "Even Parity")
        self.assertEqual(find_Parity(-7), "Odd Parity")
        self.assertEqual(find_Parity(-8), "Even Parity")
        self.assertEqual(find_Parity(-9), "Odd Parity")
        self.assertEqual(find_Parity(-10), "Even Parity")
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Parity("invalid")
        with self.assertRaises(TypeError):
            find_Parity(None)
        with self.assertRaises(TypeError):
            find_Parity([1, 2, 3])
