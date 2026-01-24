import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_no_of_ways(3, 2), 4)
        self.assertEqual(count_no_of_ways(4, 3), 15)
        self.assertEqual(count_no_of_ways(5, 4), 40)

    def test_edge_cases(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 2)
        self.assertEqual(count_no_of_ways(1, 100), 1)
        self.assertEqual(count_no_of_ways(2, 100), 2)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_no_of_ways("3", 2)
        with self.assertRaises(TypeError):
            count_no_of_ways(3, "2")
        with self.assertRaises(ValueError):
            count_no_of_ways(0, 2)
        with self.assertRaises(ValueError):
            count_no_of_ways(3, 0)
