import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 3, 5), [])

    def test_single_element(self):
        self.assertListEqual(div_of_nums([1], 3, 5), [])
        self.assertListEqual(div_of_nums([5], 3, 5), [5])
        self.assertListEqual(div_of_nums([3], 3, 5), [3])

    def test_multiple_elements(self):
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6], 3, 5), [3, 5, 6])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6], 5, 3), [5, 6])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6], 2, 3), [2])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5, 6], 4, 4), [4])
