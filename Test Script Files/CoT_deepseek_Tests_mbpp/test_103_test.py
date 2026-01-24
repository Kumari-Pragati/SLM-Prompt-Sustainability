import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_zero_n_zero_m(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_zero_n_non_zero_m(self):
        self.assertEqual(eulerian_num(0, 1), 0)

    def test_non_zero_n_zero_m(self):
        self.assertEqual(eulerian_num(1, 0), 1)

    def test_typical_cases(self):
        self.assertEqual(eulerian_num(2, 1), 2)
        self.assertEqual(eulerian_num(3, 2), 6)

    def test_edge_cases(self):
        self.assertEqual(eulerian_num(10, 9), 10*9*8*7*6*5*4*3*2)
        self.assertEqual(eulerian_num(10, 10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            eulerian_num("1", 1)
        with self.assertRaises(TypeError):
            eulerian_num(1, "1")
        with self.assertRaises(TypeError):
            eulerian_num("1", "1")
        with self.assertRaises(ValueError):
            eulerian_num(-1, 1)
        with self.assertRaises(ValueError):
            eulerian_num(1, -1)
        with self.assertRaises(ValueError):
            eulerian_num(-1, -1)
