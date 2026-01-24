import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 3, 4), [])

    def test_single_element(self):
        self.assertListEqual(div_of_nums([10], 3, 4), [])
        self.assertListEqual(div_of_nums([12], 3, 4), [12])
        self.assertListEqual(div_of_nums([15], 3, 5), [15])

    def test_multiple_elements(self):
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15], 3, 4), [12, 15])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18], 3, 9), [18])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 27], 3, 9), [18, 27])
