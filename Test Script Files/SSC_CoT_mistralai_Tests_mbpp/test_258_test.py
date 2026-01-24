import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)
        self.assertEqual(count_odd([-1, -3, -5, -7]), 4)
        self.assertEqual(count_odd([0, 2, 4, 6]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_odd([]), 0)
        self.assertEqual(count_odd([1]), 1)
        self.assertEqual(count_odd([2, 2, 2]), 0)
        self.assertEqual(count_odd([-1, 1, -1, 1]), 2)

    def test_special_cases(self):
        self.assertEqual(count_odd([1.5, 3, 5]), 2)
        self.assertEqual(count_odd([-1, 0, 1]), 1)
        self.assertEqual(count_odd([-1, -2, -3]), 3)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_odd, 'abc')
        self.assertRaises(TypeError, count_odd, [1, 'a'])
