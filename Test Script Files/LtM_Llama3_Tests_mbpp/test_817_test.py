import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(div_of_nums([], 2, 3), [])

    def test_single_element_input(self):
        self.assertEqual(div_of_nums([5], 2, 3), [])

    def test_divisible_by_m(self):
        self.assertEqual(div_of_nums([10, 20, 30], 2, 3), [10, 20, 30])

    def test_divisible_by_n(self):
        self.assertEqual(div_of_nums([15, 30, 45], 2, 3), [15, 30, 45])

    def test_divisible_by_both(self):
        self.assertEqual(div_of_nums([10, 20, 30, 45], 2, 3), [10, 20, 30, 45])

    def test_divisible_by_m_and_n(self):
        self.assertEqual(div_of_nums([15, 30, 45, 60], 2, 3), [15, 30, 45, 60])

    def test_divisible_by_m_or_n(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 2, 3), [10, 20, 30, 40, 50])

    def test_divisible_by_m_and_not_n(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 2, 5), [10, 20, 30, 40])

    def test_divisible_by_n_and_not_m(self):
        self.assertEqual(div_of_nums([15, 30, 45, 60], 2, 5), [30, 45, 60])

    def test_divisible_by_m_and_n_and_not_both(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50, 60], 2, 5), [10, 20, 30, 40, 50])

    def test_divisible_by_m_or_n_and_not_both(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50, 60], 2, 3), [10, 20, 30, 40, 50, 60])
