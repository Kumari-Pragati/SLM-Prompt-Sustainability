import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_no_negative_numbers(self):
        self.assertEqual(remove_negs([1, 2, 3]), [1, 2, 3])

    def test_single_negative_number(self):
        self.assertEqual(remove_negs([-1, 2, 3]), [2, 3])

    def test_multiple_negative_numbers(self):
        self.assertEqual(remove_negs([-1, -2, 3, 4]), [3, 4])

    def test_negative_numbers_at_start(self):
        self.assertEqual(remove_negs([-1, -2, 3, 4]), [3, 4])

    def test_negative_numbers_at_end(self):
        self.assertEqual(remove_negs([1, 2, 3, -4]), [1, 2, 3])

    def test_negative_numbers_in_middle(self):
        self.assertEqual(remove_negs([1, -2, 3, 4]), [1, 3, 4])

    def test_negative_numbers_everywhere(self):
        self.assertEqual(remove_negs([-1, -2, -3, 4, 5]), [4, 5])
