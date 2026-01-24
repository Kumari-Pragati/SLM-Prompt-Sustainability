import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_sum_elements_typical(self):
        self.assertEqual(sum_elements((1, 2, 3, 4, 5)), 15)

    def test_sum_elements_empty(self):
        self.assertEqual(sum_elements(()), 0)

    def test_sum_elements_single(self):
        self.assertEqual(sum_elements((1,)), 1)

    def test_sum_elements_negative(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_sum_elements_mixed(self):
        self.assertEqual(sum_elements((1, -2, 3, -4)), -2)

    def test_sum_elements_large(self):
        self.assertEqual(sum_elements(range(1, 100)), 4950)

    def test_sum_elements_non_int(self):
        with self.assertRaises(TypeError):
            sum_elements(("a", "b", "c"))
