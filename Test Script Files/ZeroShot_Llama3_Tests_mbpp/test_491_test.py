import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):

    def test_sum_gp(self):
        self.assertAlmostEqual(sum_gp(1, 2, 0.5), 1.5, places=5)
        self.assertAlmostEqual(sum_gp(2, 3, 0.3), 3.5499999999999996, places=5)
        self.assertAlmostEqual(sum_gp(5, 4, 0.2), 10.0, places=5)
        self.assertAlmostEqual(sum_gp(10, 5, 0.1), 21.0, places=5)
        self.assertAlmostEqual(sum_gp(20, 10, 0.05), 50.0, places=5)
        self.assertAlmostEqual(sum_gp(100, 20, 0.01), 200.0, places=5)

    def test_sum_gp_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_gp('a', 2, 0.5)
        with self.assertRaises(TypeError):
            sum_gp(1, 'b', 0.5)
        with self.assertRaises(TypeError):
            sum_gp(1, 2, 'c')
