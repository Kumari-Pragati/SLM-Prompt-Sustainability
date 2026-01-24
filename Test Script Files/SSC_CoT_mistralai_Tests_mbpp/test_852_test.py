import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_all_negative_input(self):
        self.assertEqual(remove_negs([-1, -2, -3]), [])

    def test_single_negative_input(self):
        self.assertEqual(remove_negs([0, -1]), [0])

    def test_negative_at_beginning(self):
        self.assertEqual(remove_negs([-1, 0, 1]), [0, 1])

    def test_negative_at_end(self):
        self.assertEqual(remove_negs([1, 0, -1]), [1, 0])

    def test_negative_in_middle(self):
        self.assertEqual(remove_negs([1, -2, 3]), [1, 3])

    def test_floats(self):
        self.assertEqual(remove_negs([0.0, -1.5, 2.3]), [0.0, 2.3])
