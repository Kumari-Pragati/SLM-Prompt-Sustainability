import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_single_integer(self):
        self.assertEqual(count_elim([1]), 1)

    def test_single_tuple(self):
        self.assertEqual(count_elim([(1, 2)]), 0)

    def test_multiple_integers(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_mixed_data_types(self):
        self.assertEqual(count_elim([1, (1, 2), 3]), 2)

    def test_list_of_tuples(self):
        self.assertEqual(count_elim([(1, 2), (3, 4)]), 0)
