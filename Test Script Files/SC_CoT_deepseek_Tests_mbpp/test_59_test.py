import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(is_octagonal(1), 1)
        self.assertEqual(is_octagonal(2), 10)
        self.assertEqual(is_octagonal(3), 27)

    def test_boundary_conditions(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(1000), 3000000)

    def test_edge_cases(self):
        self.assertEqual(is_octagonal(10000), 300000000)
        self.assertEqual(is_octagonal(100000), 30000000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal('1')
        with self.assertRaises(TypeError):
            is_octagonal(None)
        with self.assertRaises(TypeError):
            is_octagonal([1])
