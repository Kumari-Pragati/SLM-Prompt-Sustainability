import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 10, 15, 25), 20)

    def test_boundary_case(self):
        self.assertEqual(sum_nums(15, 15, 15, 30), 20)
        self.assertEqual(sum_nums(10, 10, 20, 30), 20)
        self.assertEqual(sum_nums(5, 5, 10, 15), 20)

    def test_edge_case(self):
        self.assertEqual(sum_nums(14, 16, 15, 30), 20)
        self.assertEqual(sum_nums(15, 14, 15, 30), 20)
        self.assertEqual(sum_nums(10, 10, 11, 20), 20)
        self.assertEqual(sum_nums(5, 5, 6, 10), 20)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_nums('5', 10, 15, 25)
        with self.assertRaises(TypeError):
            sum_nums(5, '10', 15, 25)
        with self.assertRaises(TypeError):
            sum_nums(5, 10, '15', 25)
        with self.assertRaises(TypeError):
            sum_nums(5, 10, 15, '25')
