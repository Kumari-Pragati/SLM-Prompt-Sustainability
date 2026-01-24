import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no_of_ways(3, 2), 3)

    def test_edge_case(self):
        self.assertEqual(count_no_of_ways(1, 2), 2)
        self.assertEqual(count_no_of_ways(2, 2), 4)

    def test_boundary_case(self):
        self.assertEqual(count_no_of_ways(4, 2), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_no_of_ways('a', 2)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            count_no_of_ways(-1, 2)
