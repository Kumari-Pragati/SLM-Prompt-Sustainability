import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)
        self.assertEqual(count_elim([1, (2, 3), 4]), 2)

    def test_edge_cases(self):
        self.assertEqual(count_elim([]), 0)
        self.assertEqual(count_elim([(1, 2), 3]), 1)
        self.assertEqual(count_elim([(1, 2), (3, 4)]), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_elim, (1, 2))
        self.assertRaises(TypeError, count_elim, "string")
