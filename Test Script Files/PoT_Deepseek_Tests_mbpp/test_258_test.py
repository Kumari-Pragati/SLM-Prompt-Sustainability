import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)
        self.assertEqual(count_odd([10, 20, 30, 40, 50]), 0)
        self.assertEqual(count_odd([1, 3, 5, 7, 9]), 5)

    def test_edge_cases(self):
        self.assertEqual(count_odd([0]), 0)
        self.assertEqual(count_odd([-1]), 1)
        self.assertEqual(count_odd([-2]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_odd([]), 0)
        self.assertEqual(count_odd([2]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_odd("1, 2, 3")
        with self.assertRaises(TypeError):
            count_odd(123)
