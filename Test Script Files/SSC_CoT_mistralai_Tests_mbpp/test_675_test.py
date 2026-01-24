import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(-3, 4, 0, 5), 7)

    def test_edge_case_sum_outside_range(self):
        self.assertNotEqual(sum_nums(5, 3, 10, 5), 20)
        self.assertNotEqual(sum_nums(-3, 4, 5, 0), 20)

    def test_edge_case_sum_equal_to_m(self):
        self.assertEqual(sum_nums(3, 0, 3, 5), 20)

    def test_edge_case_sum_equal_to_n(self):
        self.assertEqual(sum_nums(5, 0, 5, 5), 20)

    def test_negative_numbers(self):
        self.assertEqual(sum_nums(-3, -4, 1, 5), -7)
        self.assertEqual(sum_nums(-3, -4, -5, 5), -7)
        self.assertEqual(sum_nums(-3, -4, -5, -5), -7)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_nums, "a", "b", 1, 2)
        self.assertRaises(TypeError, sum_nums, 1, "b", 1, 2)
        self.assertRaises(TypeError, sum_nums, 1, 2, "a", 2)
