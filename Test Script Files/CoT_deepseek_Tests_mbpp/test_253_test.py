import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_mixed_list(self):
        self.assertEqual(count_integer([1, '2', 3.0, 4, None]), 2)

    def test_list_with_non_integer_elements(self):
        self.assertEqual(count_integer([1, 2, 3, 4, '5']), 4)

    def test_list_with_integer_sublists(self):
        self.assertEqual(count_integer([[1, 2], [3, 4], [5]]), 3)

    def test_list_with_integer_tuples(self):
        self.assertEqual(count_integer([(1, 2), (3, 4), (5)]), 3)

    def test_list_with_integer_dicts(self):
        self.assertEqual(count_integer([{'a': 1}, {'b': 2}, {'c': 3}]), 0)

    def test_list_with_integer_and_none(self):
        self.assertEqual(count_integer([1, None]), 1)

    def test_list_with_integer_and_string(self):
        self.assertEqual(count_integer([1, '2']), 1)

    def test_list_with_integer_and_float(self):
        self.assertEqual(count_integer([1, 2.0]), 1)

    def test_list_with_integer_and_boolean(self):
        self.assertEqual(count_integer([1, True]), 1)
        self.assertEqual(count_integer([1, False]), 1)
