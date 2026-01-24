import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 15, 18])
        self.assertEqual(large_product([-1, 0, 1], [-2, 0, 2], 3), [2, 0, -2])

    def test_edge_cases(self):
        self.assertEqual(large_product([], [], 0), [])
        self.assertEqual(large_product([1], [], 1), [])
        self.assertEqual(large_product([], [1], 1), [])

    def test_max_value(self):
        self.assertEqual(large_product([10, 20, 30], [40, 50, 60], 3), [600, 600, 600])

    def test_min_value(self):
        self.assertEqual(large_product([-10, -20, -30], [-40, -50, -60], 3), [-1200, -1200, -1200])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            large_product(None, [1, 2, 3], 3)
        with self.assertRaises(TypeError):
            large_product([1, 2, 3], None, 3)
        with self.assertRaises(TypeError):
            large_product([1, 2, 3], [1, 2, 3], 'a')
