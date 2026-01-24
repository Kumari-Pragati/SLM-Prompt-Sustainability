import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_no_negatives(self):
        self.assertEqual(remove_negs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_single_negative(self):
        self.assertEqual(remove_negs([1, 2, -3, 4, 5]), [1, 2, 4, 5])

    def test_multiple_negatives(self):
        self.assertEqual(remove_negs([-1, -2, 3, -4, 5]), [3, 5])

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_all_negatives(self):
        self.assertEqual(remove_negs([-1, -2, -3, -4, -5]), [])

    def test_mixed_list(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            remove_negs("not a list")

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            remove_negs([1, "not an integer", 3, 4, 5])
