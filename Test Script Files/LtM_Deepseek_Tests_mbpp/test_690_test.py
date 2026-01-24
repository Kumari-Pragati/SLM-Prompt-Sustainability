import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6, 12])
        self.assertEqual(mul_consecutive_nums([5, 10, 15]), [100, 225])

    def test_edge_conditions(self):
        self.assertEqual(mul_consecutive_nums([1]), [])
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_boundary_conditions(self):
        self.assertEqual(mul_consecutive_nums([0, 0]), [0])
        self.assertEqual(mul_consecutive_nums([-1, -2]), [2])

    def test_complex_cases(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12, 20])
        self.assertEqual(mul_consecutive_nums([10, 20, 30, 40]), [200, 600])
