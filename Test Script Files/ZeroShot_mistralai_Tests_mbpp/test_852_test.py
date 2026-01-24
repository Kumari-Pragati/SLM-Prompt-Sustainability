import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_negs([]), [])

    def test_positive_list(self):
        self.assertListEqual(remove_negs([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_negative_list(self):
        self.assertListEqual(remove_negs([-1, -2, 3, -4]), [3])

    def test_mixed_list(self):
        self.assertListEqual(remove_negs([-1, 1, -2, 2, -3, 3]), [1, 2, 3])

    def test_duplicates(self):
        self.assertListEqual(remove_negs([-1, -1, 1, 1]), [1])
