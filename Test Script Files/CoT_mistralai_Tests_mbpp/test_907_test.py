import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(lucky_num(0), [])

    def test_single_element(self):
        self.assertListEqual(lucky_num(1), [1])

    def test_small_positive_numbers(self):
        self.assertListEqual(lucky_num(2), [1, 3])
        self.assertListEqual(lucky_num(3), [1, 3, 5])
        self.assertListEqual(lucky_num(4), [1, 3, 5, 7])

    def test_large_positive_numbers(self):
        self.assertListEqual(lucky_num(10), [1, 3, 5, 7, 9])
        self.assertListEqual(lucky_num(100), [1, 3, 5, 7, 9, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97])

    def test_negative_numbers(self):
        self.assertListEqual(lucky_num(-1), [1])
        self.assertListEqual(lucky_num(-2), [1, 3])
        self.assertListEqual(lucky_num(-3), [1, 3, 5])

    def test_edge_cases(self):
        self.assertListEqual(lucky_num(1000), [1, 3, 5, 7, 9, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97])
        self.assertListEqual(lucky_num(10000), [1, 3, 5, 7, 9, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249,