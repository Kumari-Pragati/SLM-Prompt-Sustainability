import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(eulerian_num(3, 1), 3)
        self.assertEqual(eulerian_num(4, 2), 6)
        self.assertEqual(eulerian_num(5, 3), 15)

    def test_edge_cases(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(2, 2), 2)
        self.assertEqual(eulerian_num(3, 3), 0)

    def test_boundary_cases(self):
        self.assertEqual(eulerian_num(0, 1), 0)
        self.assertEqual(eulerian_num(1, 1), 1)
        self.assertEqual(eulerian_num(2, 2), 2)
        self.assertEqual(eulerian_num(3, 3), 0)
