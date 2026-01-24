import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_ways(4), 1)
        self.assertEqual(find_ways(6), 4)

    def test_edge_cases(self):
        self.assertEqual(find_ways(0), 0)
        self.assertEqual(find_ways(1), 0)
        self.assertEqual(find_ways(2), 0)
        self.assertEqual(find_ways(3), 0)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            find_ways('a')
        with self.assertRaises(ValueError):
            find_ways(-1)
