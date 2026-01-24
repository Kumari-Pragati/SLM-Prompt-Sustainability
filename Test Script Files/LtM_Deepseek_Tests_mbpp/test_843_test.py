import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 3, 5]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2, 3, 5]), 2)
        self.assertEqual(nth_super_ugly_number(4, [2, 3, 5]), 4)
        self.assertEqual(nth_super_ugly_number(5, [2, 3, 5]), 4)

    def test_edge_conditions(self):
        self.assertEqual(nth_super_ugly_number(0, [2, 3, 5]), 0)
        self.assertEqual(nth_super_ugly_number(1, []), 1)

    def test_boundary_conditions(self):
        self.assertEqual(nth_super_ugly_number(1000, [2, 3, 5]), 536870912)
        self.assertEqual(nth_super_ugly_number(1000, [7, 11, 13, 19]), 10399898888443)

    def test_complex_cases(self):
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 13, 19]), 207361536)
        self.assertEqual(nth_super_ugly_number(100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), 5120000000)
