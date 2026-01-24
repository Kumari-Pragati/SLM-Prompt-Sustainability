import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(eulerian_num(3, 2), 2)
        self.assertEqual(eulerian_num(4, 2), 6)

    def test_edge_conditions(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(5, 0), 1)
        self.assertEqual(eulerian_num(3, 3), 0)

    def test_complex_cases(self):
        self.assertEqual(eulerian_num(5, 3), 10)
        self.assertEqual(eulerian_num(6, 4), 30)
