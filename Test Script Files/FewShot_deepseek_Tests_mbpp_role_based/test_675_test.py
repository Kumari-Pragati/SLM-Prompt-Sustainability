import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_nums(5, 10, 15, 25), 20)

    def test_boundary_conditions(self):
        self.assertEqual(sum_nums(15, 15, 30, 30), 30)
        self.assertEqual(sum_nums(0, 0, 0, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(sum_nums(-10, 10, -5, 5), 0)
        self.assertEqual(sum_nums(1000, 1000, 2000, 2000), 2000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_nums('5', 10, 15, 25)
        with self.assertRaises(TypeError):
            sum_nums(5, '10', 15, 25)
        with self.assertRaises(TypeError):
            sum_nums(5, 10, '15', 25)
        with self.assertRaises(TypeError):
            sum_nums(5, 10, 15, '25')
