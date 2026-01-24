import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_no_of_ways(3, 2), 6)
        self.assertEqual(count_no_of_ways(4, 3), 36)

    def test_edge_cases(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(1, 100), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_no_of_ways(0, 100), 0)
        self.assertEqual(count_no_of_ways(200, 100), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_no_of_ways("3", 2)
        with self.assertRaises(TypeError):
            count_no_of_ways(3, "2")
        with self.assertRaises(ValueError):
            count_no_of_ways(-1, 2)
        with self.assertRaises(ValueError):
            count_no_of_ways(3, -1)
