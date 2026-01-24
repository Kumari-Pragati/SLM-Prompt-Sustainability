import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(eulerian_num(5, 2), 10)

    def test_boundary_conditions(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(5, 5), 0)

    def test_edge_conditions(self):
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(1, 1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            eulerian_num('5', 2)
        with self.assertRaises(TypeError):
            eulerian_num(5, '2')
        with self.assertRaises(TypeError):
            eulerian_num('5', '2')
