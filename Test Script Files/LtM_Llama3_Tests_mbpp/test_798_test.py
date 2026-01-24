import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(_sum([]), 0)

    def test_single_element_array(self):
        self.assertEqual(_sum([1]), 1)

    def test_multiple_elements_array(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

    def test_negative_elements_array(self):
        self.assertEqual(_sum([-1, -2, -3]), -6)

    def test_mixed_elements_array(self):
        self.assertEqual(_sum([1, -2, 3, -4]), 0)

    def test_large_elements_array(self):
        self.assertEqual(_sum([100, 200, 300]), 600)

    def test_small_elements_array(self):
        self.assertEqual(_sum([-100, -200, -300]), -600)
