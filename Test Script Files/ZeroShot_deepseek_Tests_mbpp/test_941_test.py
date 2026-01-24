import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_count_elim_with_list(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_count_elim_with_tuple(self):
        self.assertEqual(count_elim((1, 2, 3)), 1)

    def test_count_elim_with_mixed_list(self):
        self.assertEqual(count_elim([1, 2, (3, 4)]), 2)

    def test_count_elim_with_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_count_elim_with_single_element(self):
        self.assertEqual(count_elim([1]), 1)
