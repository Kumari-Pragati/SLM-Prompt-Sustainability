import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_val([0, 9, 2, 5, 1]), 9)

    def test_edge_cases(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5, 5]), 5)
        self.assertEqual(max_val([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_val([5, -1, 3, -2, 1]), 5)
        self.assertEqual(max_val([5, 4, 3, 2, 1, 0]), 5)
        self.assertEqual(max_val([5, 4, 3, 2, 1, -1]), 5)

    def test_boundary_cases(self):
        self.assertEqual(max_val([-5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_val([0, -1, -2, -3, -4]), -1)
        self.assertEqual(max_val([-5, -4, -3, -2, -1, -1]), -1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, max_val, [1, "two", 3])
        self.assertRaises(TypeError, max_val, ["one", 2, 3])
        self.assertRaises(TypeError, max_val, [1, 2, "three"])
