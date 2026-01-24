import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(sum_nums(5, 10, 10, 20), 20)
        self.assertEqual(sum_nums(10, 5, 10, 20), 20)
        self.assertEqual(sum_nums(15, 15, 10, 20), 20)

    def test_edge_cases(self):
        self.assertEqual(sum_nums(20, 5, 10, 20), 25)
        self.assertEqual(sum_nums(5, 20, 10, 20), 25)
        self.assertEqual(sum_nums(10, 10, 10, 20), 20)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_nums('a', 5, 10, 20)
        with self.assertRaises(TypeError):
            sum_nums(5, 'a', 10, 20)
        with self.assertRaises(TypeError):
            sum_nums(5, 5, 'a', 20)
        with self.assertRaises(TypeError):
            sum_nums(5, 5, 10, 'a')

    def test_range_conditions(self):
        self.assertEqual(sum_nums(5, 10, 5, 15), 15)
        self.assertEqual(sum_nums(10, 5, 5, 15), 15)
        self.assertEqual(sum_nums(15, 5, 5, 15), 20)
