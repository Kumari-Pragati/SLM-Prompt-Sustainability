import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_elim((1, 2, 3, 4)), 4)

    def test_empty_case(self):
        self.assertEqual(count_elim(()), 0)

    def test_single_tuple_case(self):
        self.assertEqual(count_elim((1, (2, 3))), 1)

    def test_nested_tuples_case(self):
        self.assertEqual(count_elim((1, (2, (3, 4)))), 2)

    def test_non_tuple_elements_case(self):
        self.assertEqual(count_elim([1, 2, 3, 4]), 0)

    def test_mixed_elements_case(self):
        self.assertEqual(count_elim([1, (2, 3), 4]), 1)

    def test_large_tuple_case(self):
        self.assertEqual(count_elim(tuple(range(1, 1001))), 1000)

    def test_invalid_input_case(self):
        with self.assertRaises(TypeError):
            count_elim(None)
