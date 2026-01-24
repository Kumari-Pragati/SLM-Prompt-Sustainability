import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)
        self.assertEqual(count_elim([1, 'a', 3]), 2)
        self.assertEqual(count_elim([1, [1, 2], 3]), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_elim([]), 0)
        self.assertEqual(count_elim([1]), 1)
        self.assertEqual(count_elim([1, 2, 3, 4, 5]), 5)

    def test_complex_cases(self):
        self.assertEqual(count_elim([1, (1, 2), 3]), 1)
        self.assertEqual(count_elim([1, [1, (2, 3)], 3]), 1)
        self.assertEqual(count_elim([1, [1, [2, 3]], 3]), 1)
