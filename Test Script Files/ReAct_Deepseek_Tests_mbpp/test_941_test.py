import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(count_elim([]), 0)

    def test_list_with_tuples(self):
        self.assertEqual(count_elim([1, 2, (3, 4)]), 2)

    def test_list_with_mixed_types(self):
        self.assertEqual(count_elim([1, 'two', 3.0]), 1)

    def test_list_with_nested_tuples(self):
        self.assertEqual(count_elim([1, (2, (3, 4))]), 1)

    def test_list_with_single_tuple(self):
        self.assertEqual(count_elim([(1, 2, 3)]), 0)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            count_elim([None])
