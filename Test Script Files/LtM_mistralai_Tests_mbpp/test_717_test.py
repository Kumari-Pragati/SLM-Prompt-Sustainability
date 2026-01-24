import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(avg_calc([1, 2, 3]), 2.0)
        self.assertEqual(avg_calc([4, 4, 4]), 4.0)

    def test_edge_cases(self):
        self.assertEqual(avg_calc([]), 0.0)
        self.assertEqual(avg_calc([0]), 0.0)
        self.assertEqual(avg_calc([-1, 0, 1]), 0.0)

    def test_boundary_cases(self):
        self.assertEqual(avg_calc([sys.maxsize, sys.maxsize, sys.maxsize]), sys.float_info.max)
        self.assertEqual(avg_calc([-sys.maxsize, -sys.maxsize, -sys.maxsize]), -sys.float_info.max)

    def test_complex_input(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(avg_calc([1000000000, 2000000000, 3000000000]), 2000000000.0)
