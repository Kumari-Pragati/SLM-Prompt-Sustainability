import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_odd([1, 2, 3]), 2)
        self.assertEqual(count_odd([2, 4, 6]), 0)
        self.assertEqual(count_odd([1]), 1)
        self.assertEqual(count_odd([2]), 0)

    def test_edge_conditions(self):
        self.assertEqual(count_odd([]), 0)
        self.assertEqual(count_odd([0]), 0)
        self.assertEqual(count_odd([-1]), 1)
        self.assertEqual(count_odd([-2]), 0)

    def test_complex_cases(self):
        self.assertEqual(count_odd([-1, -2, -3]), 3)
        self.assertEqual(count_odd([0, 2, 4]), 0)
        self.assertEqual(count_odd([-1, 0, 1]), 2)
        self.assertEqual(count_odd([2, 3, 4, 5, 6]), 2)
