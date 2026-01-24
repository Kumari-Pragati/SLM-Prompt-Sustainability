import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(2, 1), 3)
        self.assertEqual(eulerian_num(3, 2), 10)

    def test_edge_cases(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(1, 1), 1)
        self.assertEqual(eulerian_num(2, 2), 4)
        self.assertEqual(eulerian_num(3, 3), 19)

    def test_boundary(self):
        self.assertEqual(eulerian_num(0, 2), 0)
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(2, 0), 0)
        self.assertEqual(eulerian_num(3, 0), 0)

    def test_negative(self):
        self.assertEqual(eulerian_num(-1, 0), None)
        self.assertEqual(eulerian_num(0, -1), None)
        self.assertEqual(eulerian_num(-1, -1), None)
