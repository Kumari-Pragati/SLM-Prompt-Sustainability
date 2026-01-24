import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_list([]), 0)

    def test_single_element_list(self):
        for num in range(-10, 11):
            self.assertEqual(max_sum_list([num]), num)

    def test_multiple_elements_positive(self):
        data = [
            ([1, 2, 3, 4], 10),
            ([10, 20, 30, 40], 50),
            ([100, 200, 300, 400], 1000),
        ]
        for test_data in data:
            self.assertEqual(max_sum_list(test_data[0]), test_data[1])

    def test_multiple_elements_negative(self):
        data = [
            ([-1, -2, -3, -4], -10),
            ([-10, -20, -30, -40], -50),
            ([-100, -200, -300, -400], -1000),
        ]
        for test_data in data:
            self.assertEqual(max_sum_list(test_data[0]), test_data[1])

    def test_mixed_elements_positive_negative(self):
        data = [
            ([1, -2, 3, -4], 3),
            ([-1, 2, -3, 4], 4),
            ([10, -20, 30, -40], 30),
            ([-10, 20, -30, 40], 40),
        ]
        for test_data in data:
            self.assertEqual(max_sum_list(test_data[0]), test_data[1])

    def test_list_with_zero(self):
        data = [
            ([0, 1, 2, 3], 3),
            ([3, 2, 1, 0], 3),
            ([0, -1, -2, -3], -3),
            ([-3, -2, -1, 0], -3),
        ]
        for test_data in data:
            self.assertEqual(max_sum_list(test_data[0]), test_data[1])
