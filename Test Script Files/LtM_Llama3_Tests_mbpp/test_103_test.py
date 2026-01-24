import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(2, 0), 1)
        self.assertEqual(eulerian_num(3, 0), 2)
        self.assertEqual(eulerian_num(4, 0), 3)
        self.assertEqual(eulerian_num(5, 0), 5)

    def test_edge_cases(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(1, 1), 0)
        self.assertEqual(eulerian_num(2, 1), 1)
        self.assertEqual(eulerian_num(3, 2), 2)
        self.assertEqual(eulerian_num(4, 3), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            eulerian_num('a', 0)
        with self.assertRaises(TypeError):
            eulerian_num(0, 'b')
