import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(nth_super_ugly_number(1, [1]), 1)
        self.assertEqual(nth_super_ugly_number(2, [1, 2]), 1)
        self.assertEqual(nth_super_ugly_number(3, [1, 2]), 2)
        self.assertEqual(nth_super_ugly_number(4, [1, 2]), 3)
        self.assertEqual(nth_super_ugly_number(5, [1, 2, 3]), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(nth_super_ugly_number(1, [1, 2, 3]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 3, 4]), 2)
        self.assertEqual(nth_super_ugly_number(3, [3, 4, 5]), 4)
        self.assertEqual(nth_super_ugly_number(4, [4, 5, 6]), 6)
        self.assertEqual(nth_super_ugly_number(5, [5, 6, 7]), 8)

    def test_special_or_corner_cases(self):
        self.assertEqual(nth_super_ugly_number(1, [1, 1, 1]), 1)
        self.assertEqual(nth_super_ugly_number(2, [1, 2, 2]), 2)
        self.assertEqual(nth_super_ugly_number(3, [1, 2, 3]), 2)
        self.assertEqual(nth_super_ugly_number(4, [1, 2, 3, 4]), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            nth_super_ugly_number(-1, [1, 2, 3])
        with self.assertRaises(TypeError):
            nth_super_ugly_number(1, ['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            nth_super_ugly_number(1, [1, 2, 3], invalid_input='test')
