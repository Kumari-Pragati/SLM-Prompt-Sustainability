import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(eulerian_num(5, 2), 20)
        self.assertEqual(eulerian_num(3, 1), 4)
        self.assertEqual(eulerian_num(4, 2), 12)

    def test_boundary_conditions(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(5, 5), 0)

    def test_edge_cases(self):
        self.assertEqual(eulerian_num(0, 1), 0)
        self.assertEqual(eulerian_num(1, 0), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            eulerian_num("5", 2)
        with self.assertRaises(TypeError):
            eulerian_num(5, "2")
        with self.assertRaises(TypeError):
            eulerian_num("5", "2")
