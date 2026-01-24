import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(count_integer([-1, 0, 2, 3, -4]), 4)
        self.assertEqual(count_integer([1, 1.0, 1+0j]), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_integer([]), 0)
        self.assertEqual(count_integer([0]), 1)
        self.assertEqual(count_integer([-1, 0, 1]), 2)
        self.assertEqual(count_integer([-1, 0, 1, 0]), 2)
        self.assertEqual(count_integer([1, 2, 3, 2, 1]), 4)

    def test_special_cases(self):
        self.assertEqual(count_integer([float('inf'), float('-inf'), 1, 2, 3]), 4)
        self.assertEqual(count_integer([complex(1, 0), complex(0, 1), 1, 2, 3]), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_integer, [1, 'a', 2])
        self.assertRaises(TypeError, count_integer, ['a', 'b', 'c'])
