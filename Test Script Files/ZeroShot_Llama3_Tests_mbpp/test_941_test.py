import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_count_elim_positive_integers(self):
        self.assertEqual(count_elim([1, 2, 3, 4, 5]), 5)

    def test_count_elim_negative_integers(self):
        self.assertEqual(count_elim([-1, -2, -3, -4, -5]), 5)

    def test_count_elim_mixed_integers(self):
        self.assertEqual(count_elim([1, -2, 3, -4, 5]), 5)

    def test_count_elim_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_count_elim_list_with_tuple(self):
        self.assertEqual(count_elim([1, 2, 3, (4, 5)]), 3)

    def test_count_elim_list_with_tuple_at_end(self):
        self.assertEqual(count_elim([1, 2, 3, 4, 5, (6, 7)]), 5)

    def test_count_elim_list_with_tuple_in_middle(self):
        self.assertEqual(count_elim([1, 2, (3, 4), 5, 6]), 3)
