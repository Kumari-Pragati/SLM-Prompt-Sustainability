import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_eulerian_num_zero(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_eulerian_num_negative(self):
        self.assertRaises(ValueError, eulerian_num, -1, 0)

    def test_eulerian_num_invalid_input(self):
        self.assertRaises(ValueError, eulerian_num, 0, -1)

    def test_eulerian_num_simple_case(self):
        self.assertEqual(eulerian_num(3, 1), 3)

    def test_eulerian_num_complex_case(self):
        self.assertEqual(eulerian_num(10, 5), 147)
