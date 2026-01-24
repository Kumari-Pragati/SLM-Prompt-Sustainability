import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(big_sum([1, 2, 3]), 3)
        self.assertEqual(big_sum([-1, 0, 1]), 0)
        self.assertEqual(big_sum([5, 5, 5]), 5)

    def test_edge_cases(self):
        self.assertEqual(big_sum([-10, 10]), 10)
        self.assertEqual(big_sum([10, 10]), 20)
        self.assertEqual(big_sum([-10, -10]), -10)

    def test_min_max_edge_cases(self):
        self.assertEqual(big_sum([-100, 100]), 100)
        self.assertEqual(big_sum([100, 100]), 200)
        self.assertEqual(big_sum([-100, -100]), -100)

    def test_single_element_list(self):
        self.assertEqual(big_sum([5]), 5)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            big_sum([])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            big_sum([1, 2, 'a'])
