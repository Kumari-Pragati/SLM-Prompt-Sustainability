import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(check('01010101'), 'Yes')
        self.assertEqual(check('11111111'), 'Yes')
        self.assertEqual(check('00000000'), 'Yes')
        
    def test_edge_cases(self):
        self.assertEqual(check(''), 'Yes')
        self.assertEqual(check('0'), 'Yes')
        self.assertEqual(check('1'), 'Yes')
        
    def test_corner_cases(self):
        self.assertEqual(check('01'), 'No')
        self.assertEqual(check('10'), 'No')
        self.assertEqual(check('0011'), 'No')
        self.assertEqual(check('1100'), 'No')
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check(12345)
        with self.assertRaises(TypeError):
            check(12345678901234567890123456789012345678901234567890123456789012345678901234567890)
