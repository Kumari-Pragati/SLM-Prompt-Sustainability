import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(div_of_nums([], 2, 3), [])

    def test_single_element_input(self):
        self.assertEqual(div_of_nums([10], 2, 3), [])

    def test_multiple_elements_input(self):
        self.assertEqual(div_of_nums([10, 20, 30], 2, 3), [30])

    def test_divisible_by_m_and_n(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 2, 3), [30, 40, 50])

    def test_divisible_by_m_only(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 2, 1), [10, 20, 30, 40])

    def test_divisible_by_n_only(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 1, 3), [30, 40, 50])

    def test_not_divisible_by_m_or_n(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [])

    def test_divisible_by_m_and_not_n(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 2, 4), [10, 20, 30, 40])

    def test_divisible_by_n_and_not_m(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 4, 3), [30, 40, 50])

    def test_divisible_by_m_and_n_and_others(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50, 60, 70, 80, 90], 2, 3), [30, 40, 50, 60, 70, 80, 90])
