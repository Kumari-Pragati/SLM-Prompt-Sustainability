import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_single_element(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)

    def test_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3, -4, -5]), 12345)

    def test_zero(self):
        self.assertEqual(multiple_to_single([0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(multiple_to_single([1, -2, 3, -4, 5]), 135)
