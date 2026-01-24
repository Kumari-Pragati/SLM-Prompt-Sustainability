import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, eulerian_num, -1, 0)

    def test_one_input(self):
        self.assertEqual(eulerian_num(1, 0), 0)
        self.assertEqual(eulerian_num(1, 1), 1)

    def test_small_positive_inputs(self):
        self.assertEqual(eulerian_num(2, 1), 1)
        self.assertEqual(eulerian_num(3, 1), 2)
        self.assertEqual(eulerian_num(3, 2), 3)

    def test_large_positive_inputs(self):
        self.assertEqual(eulerian_num(10, 1), 45)
        self.assertEqual(eulerian_num(10, 2), 144)
        self.assertEqual(eulerian_num(10, 3), 360)

    def test_m_greater_than_n(self):
        self.assertEqual(eulerian_num(5, 6), 0)
        self.assertEqual(eulerian_num(10, 11), 0)
