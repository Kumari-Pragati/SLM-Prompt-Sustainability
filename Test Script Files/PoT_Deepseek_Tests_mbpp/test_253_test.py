import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_integer([1, 2, 3, 4]), 4)
        self.assertEqual(count_integer([1, 'a', 3.5, 4]), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_integer([]), 0)
        self.assertEqual(count_integer([None]), 0)
        self.assertEqual(count_integer([1]), 1)

    def test_corner_cases(self):
        self.assertEqual(count_integer([0]), 1)
        self.assertEqual(count_integer([-1]), 1)
        self.assertEqual(count_integer([1, -1]), 2)
