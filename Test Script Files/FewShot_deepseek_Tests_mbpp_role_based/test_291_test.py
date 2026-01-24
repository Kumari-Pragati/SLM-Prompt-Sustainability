import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_no_of_ways(3, 2), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 2)

    def test_edge_conditions(self):
        self.assertEqual(count_no_of_ways(0, 1), 0)
        self.assertEqual(count_no_of_ways(1, 0), 0)
        self.assertEqual(count_no_of_ways(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_no_of_ways('3', 2)
        with self.assertRaises(TypeError):
            count_no_of_ways(3, '2')
        with self.assertRaises(ValueError):
            count_no_of_ways(-1, 2)
        with self.assertRaises(ValueError):
            count_no_of_ways(3, -1)
