import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)
        self.assertEqual(count_elim([1, 2, 3, 4]), 4)
        self.assertEqual(count_elim([1, 2, 3, 4, 5]), 5)

    def test_edge(self):
        self.assertEqual(count_elim([]), 0)
        self.assertEqual(count_elim([1]), 1)
        self.assertEqual(count_elim([1, 2, 3, 4, 5, 6]), 6)

    def test_tuple_break(self):
        self.assertEqual(count_elim([(1, 2), 3, 4]), 1)
        self.assertEqual(count_elim([1, (2, 3), 4]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_elim("hello")
        with self.assertRaises(TypeError):
            count_elim(None)
