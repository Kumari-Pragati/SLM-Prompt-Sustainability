import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_positive_list(self):
        self.assertEqual(remove_negs([1, 2, 3, -1, 4, -2]), [1, 3, 4])

    def test_negative_list(self):
        self.assertEqual(remove_negs([-1, -2, -3]), [])

    def test_single_negative_item(self):
        self.assertEqual(remove_negs([0, -1]), [0])

    def test_duplicate_negative_items(self):
        self.assertEqual(remove_negs([-1, -1, 0, 1, -2, -2]), [0, 1])

    def test_list_with_zero(self):
        self.assertEqual(remove_negs([0, -1, 0, 1]), [1])

    def test_list_with_only_negative_numbers(self):
        self.assertEqual(remove_negs([-10, -20, -30]), [])

    def test_list_with_large_positive_and_negative_numbers(self):
        self.assertEqual(remove_negs([1000000, -2000000, 3000000, -4000000]), [1000000, 3000000])

    def test_list_with_floats(self):
        self.assertEqual(remove_negs([3.14, -1.618, 2.718]), [3.14, 2.718])

    def test_list_with_negative_floats(self):
        self.assertEqual(remove_negs([-3.14, -1.618, -2.718]), [])
