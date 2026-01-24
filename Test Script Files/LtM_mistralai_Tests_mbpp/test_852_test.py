import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_simple_positive_list(self):
        self.assertListEqual(remove_negs([1, 2, 3, -1, 4]), [1, 2, 3, 4])

    def test_simple_negative_list(self):
        self.assertListEqual(remove_negs([-1, -2, -3]), [])

    def test_empty_list(self):
        self.assertListEqual(remove_negs([]), [])

    def test_single_negative_list(self):
        self.assertListEqual(remove_negs([-1]), [])

    def test_min_value(self):
        self.assertListEqual(remove_negs([-2147483648]), [])

    def test_max_value(self):
        self.assertListEqual(remove_negs([2147483647]), [2147483647])

    def test_mixed_list(self):
        self.assertListEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])
