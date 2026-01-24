import unittest

from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_list_with_non_integer_elements(self):
        self.assertEqual(count_integer([1, '2', 3.0, 4, None]), 3)

    def test_list_with_mixed_integer_types(self):
        self.assertEqual(count_integer([1, 2, int('3'), int(3.0), int(True)]), 5)

    def test_list_with_negative_integers(self):
        self.assertEqual(count_integer([-1, -2, -3, -4, -5]), 5)

    def test_list_with_zero(self):
        self.assertEqual(count_integer([0]), 1)

    def test_list_with_large_integers(self):
        self.assertEqual(count_integer([1000000000000000000000000000000, -1000000000000000000000000000000]), 2)

    def test_list_with_non_integer_objects(self):
        with self.assertRaises(TypeError):
            count_integer([1, [2, 3], {4, 5}, (6, 7), {8: 9}])
