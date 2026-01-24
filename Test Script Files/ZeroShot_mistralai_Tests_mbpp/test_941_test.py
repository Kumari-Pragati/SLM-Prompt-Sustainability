import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_single_element(self):
        self.assertEqual(count_elim([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_list_with_tuple(self):
        self.assertEqual(count_elim([(1, 2), 3]), 1)

    def test_list_with_multiple_tuples(self):
        self.assertEqual(count_elim([(1, 2), (3, 4), 5]), 2)
