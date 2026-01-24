import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 2)
        self.assertEqual(count_ways(3), 4)
        self.assertEqual(count_ways(4), 8)

    def test_edge_cases(self):
        self.assertEqual(count_ways(-1), 1)
        self.assertEqual(count_ways(-2), 0)
        self.assertEqual(count_ways(-3), 2)
        self.assertEqual(count_ways(-4), 4)
        self.assertEqual(count_ways(-5), 8)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_ways('a')
        with self.assertRaises(TypeError):
            count_ways(None)
