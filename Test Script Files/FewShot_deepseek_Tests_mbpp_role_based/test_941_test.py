import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_elim([1, 2, 3, 4]), 4)

    def test_edge_condition(self):
        self.assertEqual(count_elim([]), 0)

    def test_boundary_condition(self):
        self.assertEqual(count_elim([1]), 1)

    def test_with_tuples(self):
        self.assertEqual(count_elim([1, 2, (3, 4)]), 2)

    def test_with_mixed_types(self):
        self.assertEqual(count_elim([1, '2', 3.0, (4,)]), 1)

    def test_with_invalid_input(self):
        with self.assertRaises(TypeError):
            count_elim(123)
