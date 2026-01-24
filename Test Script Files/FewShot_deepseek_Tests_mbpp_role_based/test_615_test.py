import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(average_tuple([(1, 2), (3, 4)]), [2.0, 3.0])

    def test_edge_condition(self):
        self.assertAlmostEqual(average_tuple([(1, 2), (3, 4), (5, 6)]), [3.0, 4.0])

    def test_boundary_condition(self):
        self.assertAlmostEqual(average_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]), [4.0, 5.0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            average_tuple([(1, 2), '3', (5, 6)])
