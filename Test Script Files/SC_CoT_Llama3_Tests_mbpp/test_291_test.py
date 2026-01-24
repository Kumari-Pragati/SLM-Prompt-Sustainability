import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 1)
        self.assertEqual(count_no_of_ways(3, 1), 1)
        self.assertEqual(count_no_of_ways(4, 1), 2)
        self.assertEqual(count_no_of_ways(5, 1), 3)

    def test_edge_cases(self):
        self.assertEqual(count_no_of_ways(0, 1), 0)
        self.assertEqual(count_no_of_ways(1, 0), 0)
        self.assertEqual(count_no_of_ways(2, 0), 0)

    def test_special_cases(self):
        self.assertEqual(count_no_of_ways(1, 2), 1)
        self.assertEqual(count_no_of_ways(2, 2), 2)
        self.assertEqual(count_no_of_ways(3, 2), 3)
        self.assertEqual(count_no_of_ways(4, 2), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_no_of_ways('a', 1)
        with self.assertRaises(TypeError):
            count_no_of_ways(1, 'a')
