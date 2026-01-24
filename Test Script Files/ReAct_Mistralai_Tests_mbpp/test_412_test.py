import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_odd([]), [])

    def test_single_element_list(self):
        for num in [1, -1]:
            self.assertListEqual(remove_odd([num]), [])

    def test_even_length_list(self):
        for nums in [
                [2, 4, 6],
                [-2, -4, -6],
                [2, -4, 6],
                [-2, 4, -6],
        ]:
            self.assertListEqual(remove_odd(nums), nums)

    def test_odd_length_list(self):
        for nums in [
                [1, 2, 4],
                [-1, -2, -4],
                [1, -2, 4],
                [-1, 2, -4],
        ]:
            self.assertListEqual(remove_odd(nums), [nums[0] if nums[0] % 2 != 0 else nums[1:]])

    def test_list_with_zero(self):
        self.assertListEqual(remove_odd([0]), [])

    def test_list_with_floats(self):
        self.assertListEqual(remove_odd([1.5, 2.0, 3.5]), [2.0])

    def test_list_with_non_numbers(self):
        self.assertRaises(TypeError, remove_odd, ['a', 1, 'b'])
