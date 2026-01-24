import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_lcm([2, 7]), 14)
        self.assertEqual(get_lcm([15, 10]), 30)
        self.assertEqual(get_lcm([3, 6, 9]), 18)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_lcm([0, 5]), 0)
        self.assertEqual(get_lcm([1, 1]), 1)
        self.assertEqual(get_lcm([2, 2]), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_lcm("2", 7)
        with self.assertRaises(TypeError):
            get_lcm([2, "7"])
        with self.assertRaises(TypeError):
            get_lcm([2, 7, "9"])
        with self.assertRaises(TypeError):
            get_lcm([2, 7, None])
