import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_max_sum(0), 0)

    def test_single_element(self):
        self.assertEqual(get_max_sum(1), 1)

    def test_small_numbers(self):
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 1)
        self.assertEqual(get_max_sum(4), 2)
        self.assertEqual(get_max_sum(5), 2)
        self.assertEqual(get_max_sum(6), 3)
        self.assertEqual(get_max_sum(7), 3)

    def test_large_numbers(self):
        self.assertEqual(get_max_sum(100), 27)
        self.assertEqual(get_max_sum(1000), 207)
        self.assertEqual(get_max_sum(10000), 1387)

    def test_large_numbers_with_powers_of_2(self):
        self.assertEqual(get_max_sum(2**10), 2**10)
        self.assertEqual(get_max_sum(2**15), 2**15)
        self.assertEqual(get_max_sum(2**20), 2**20)

    def test_large_numbers_with_powers_of_3(self):
        self.assertEqual(get_max_sum(3**5), 3**5)
        self.assertEqual(get_max_sum(3**10), 3**10)
        self.assertEqual(get_max_sum(3**15), 3**15)

    def test_large_numbers_with_powers_of_4(self):
        self.assertEqual(get_max_sum(4**5), 4**5)
        self.assertEqual(get_max_sum(4**10), 4**10)
        self.assertEqual(get_max_sum(4**15), 4**15)

    def test_large_numbers_with_powers_of_5(self):
        self.assertEqual(get_max_sum(5**5), 5**5)
        self.assertEqual(get_max_sum(5**10), 5**10)
        self.assertEqual(get_max_sum(5**15), 5**15)

    def test_negative_numbers(self):
        self.assertEqual(get_max_sum(-1), 0)
        self.assertEqual(get_max_sum(-2), 0)
        self.assertEqual(get_max_sum(-3), 1)

    def test_large_negative_numbers(self):
        self.assertEqual(get_max_sum(-100), 0)
        self.assertEqual(get_max_sum(-1000), 0)
        self.assertEqual(get_max_sum(-10000), 0)
