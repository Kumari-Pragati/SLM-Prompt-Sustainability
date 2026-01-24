import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_eulerian_num_normal(self):
        self.assertEqual(eulerian_num(4, 2), 6)
        self.assertEqual(eulerian_num(5, 3), 14)
        self.assertEqual(eulerian_num(6, 4), 30)

    def test_eulerian_num_edge_cases(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(2, 2), 3)
        self.assertEqual(eulerian_num(3, 3), 7)

    def test_eulerian_num_boundary_cases(self):
        self.assertEqual(eulerian_num(1, 1), 1)
        self.assertEqual(eulerian_num(2, 2), 3)
        self.assertEqual(eulerian_num(3, 3), 7)
        self.assertEqual(eulerian_num(4, 4), 20)

    def test_eulerian_num_invalid_inputs(self):
        with self.assertRaises(ValueError):
            eulerian_num(-1, 0)
        with self.assertRaises(ValueError):
            eulerian_num(0, -1)
