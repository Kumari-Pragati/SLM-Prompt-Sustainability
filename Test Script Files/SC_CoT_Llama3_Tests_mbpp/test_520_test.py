import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(get_lcm([2, 3]), 6)
        self.assertEqual(get_lcm([4, 5]), 20)
        self.assertEqual(get_lcm([6, 8]), 24)

    def test_edge_cases(self):
        self.assertEqual(get_lcm([1, 1]), 1)
        self.assertEqual(get_lcm([2, 2]), 2)
        self.assertEqual(get_lcm([3, 3]), 3)

    def test_boundary_cases(self):
        self.assertEqual(get_lcm([1, 4]), 4)
        self.assertEqual(get_lcm([2, 3]), 6)
        self.assertEqual(get_lcm([4, 5]), 20)

    def test_special_cases(self):
        self.assertEqual(get_lcm([5, 10]), 10)
        self.assertEqual(get_lcm([10, 15]), 30)
        self.assertEqual(get_lcm([20, 25]), 100)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_lcm('abc')
        with self.assertRaises(TypeError):
            get_lcm([1, 'abc'])
        with self.assertRaises(TypeError):
            get_lcm(['abc', 2])
