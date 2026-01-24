import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_simple_integer(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_simple_list(self):
        self.assertEqual(count_elim([1, (2, 3), 4]), 2)

    def test_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_single_tuple(self):
        self.assertEqual(count_elim([(1, 2), 3]), 1)

    def test_single_integer_and_tuple(self):
        self.assertEqual(count_elim([1, (1, 2)]), 1)

    def test_all_tuples(self):
        self.assertEqual(count_elim([(1, 2), (3, 4)]), 0)

    def test_complex_list(self):
        self.assertEqual(count_elim([1, (1, 2), (3, 4), 5]), 3)
