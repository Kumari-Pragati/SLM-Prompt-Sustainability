import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_count_single_value(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (3, 4)], 1), 2)

    def test_count_multiple_values(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (3, 4), (1, 2)], (1, 2)), 3)

    def test_count_empty_list(self):
        self.assertEqual(count_tuplex([], 1), 0)

    def test_count_nonexistent_value(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (3, 4)], 3), 0)

    def test_count_non_tuple_input(self):
        with self.assertRaises(TypeError):
            count_tuplex('not a tuple', 1)
