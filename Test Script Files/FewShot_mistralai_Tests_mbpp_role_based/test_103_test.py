import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_negative_n(self):
        self.assertEqual(eulerian_num(-1, 0), 0)

    def test_negative_m(self):
        self.assertEqual(eulerian_num(1, -1), 0)

    def test_m_greater_than_n(self):
        self.assertEqual(eulerian_num(1, 2), 0)

    def test_eulerian_num_1(self):
        self.assertEqual(eulerian_num(1, 0), 1)

    def test_eulerian_num_2(self):
        self.assertEqual(eulerian_num(2, 1), 1)

    def test_eulerian_num_3(self):
        self.assertEqual(eulerian_num(3, 2), 4)
