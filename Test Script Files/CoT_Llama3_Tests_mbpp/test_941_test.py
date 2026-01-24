import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_tuple_break(self):
        self.assertEqual(count_elim([(1, 2), 3, 4]), 1)

    def test_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_single_element(self):
        self.assertEqual(count_elim([1]), 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_elim("hello")

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            count_elim(123)
