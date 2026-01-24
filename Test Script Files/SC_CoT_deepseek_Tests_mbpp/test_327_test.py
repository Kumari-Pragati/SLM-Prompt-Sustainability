import unittest

from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    
    def test_typical_isosceles(self):
        self.assertTrue(check_isosceles(5,5,6))
        self.assertTrue(check_isosceles(6,7,6))
        self.assertTrue(check_isosceles(7,8,7))

    def test_typical_scalene(self):
        self.assertFalse(check_isosceles(5,6,7))
        self.assertFalse(check_isosceles(7,8,9))

    def test_edge_cases(self):
        self.assertTrue(check_isosceles(0,0,0))
        self.assertFalse(check_isosceles(1,2,3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_isosceles("a", 5, 6)
        with self.assertRaises(TypeError):
            check_isosceles(5, "b", 6)
        with self.assertRaises(TypeError):
            check_isosceles(5, 6, "c")
        with self.assertRaises(TypeError):
            check_isosceles("a", "b", "c")
        with self.assertRaises(TypeError):
            check_isosceles(5, "b", "c")
        with self.assertRaises(TypeError):
            check_isosceles("a", 5, "c")
