import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_eulerian_num_zero(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_eulerian_num_one(self):
        self.assertEqual(eulerian_num(1, 0), 1)

    def test_eulerian_num_two(self):
        self.assertEqual(eulerian_num(2, 0), 1)

    def test_eulerian_num_three(self):
        self.assertEqual(eulerian_num(3, 0), 1)

    def test_eulerian_num_four(self):
        self.assertEqual(eulerian_num(4, 0), 1)

    def test_eulerian_num_five(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_eulerian_num_six(self):
        self.assertEqual(eulerian_num(6, 0), 1)

    def test_eulerian_num_seven(self):
        self.assertEqual(eulerian_num(7, 0), 1)

    def test_eulerian_num_eight(self):
        self.assertEqual(eulerian_num(8, 0), 1)

    def test_eulerian_num_nine(self):
        self.assertEqual(eulerian_num(9, 0), 1)

    def test_eulerian_num_ten(self):
        self.assertEqual(eulerian_num(10, 0), 1)

    def test_eulerian_num_m_greater_n(self):
        self.assertEqual(eulerian_num(5, 6), 0)

    def test_eulerian_num_m_equal_n(self):
        self.assertEqual(eulerian_num(5, 5), 0)

    def test_eulerian_num_m_less_n(self):
        self.assertEqual(eulerian_num(5, 4), 5)

    def test_eulerian_num_m_equal_zero(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_eulerian_num_n_equal_zero(self):
        self.assertEqual(eulerian_num(0, 5), 0)
