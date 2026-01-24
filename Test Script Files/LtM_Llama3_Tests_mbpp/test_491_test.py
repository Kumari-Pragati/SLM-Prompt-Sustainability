import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_gp(10, 5, 0.1), 54.54545454545455)
        self.assertEqual(sum_gp(20, 3, 0.2), 60.0)
        self.assertEqual(sum_gp(5, 2, 0.3), 7.5)

    def test_edge_cases(self):
        self.assertEqual(sum_gp(0, 0, 0.1), 0.0)
        self.assertEqual(sum_gp(10, 0, 0.1), 10.0)
        self.assertEqual(sum_gp(10, 5, 1.0), 10.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_gp('a', 5, 0.1)
        with self.assertRaises(TypeError):
            sum_gp(10, 'b', 0.1)
        with self.assertRaises(TypeError):
            sum_gp(10, 5, 'c')
