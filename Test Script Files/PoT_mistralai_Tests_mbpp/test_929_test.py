import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (3, 4)], 1), 2)
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (3, 4)], 2), 0)
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (3, 4)], 3), 0)
        self.assertEqual(count_tuplex([], 1), 0)
        self.assertEqual(count_tuplex([(1, 2)], 1), 1)

    def test_edge_case(self):
        self.assertEqual(count_tuplex([(1, 2)], (1, 2)), 1)
        self.assertEqual(count_tuplex([(1, 2)], (1, 3)), 0)

    def test_boundary_case(self):
        self.assertEqual(count_tuplex([], value=1), 0)
        self.assertEqual(count_tuplex([(1, 2)], value=1), 1)
        self.assertEqual(count_tuplex([(1, 2)], value=3), 0)
