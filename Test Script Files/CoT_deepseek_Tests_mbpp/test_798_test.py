import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):

    def test_list_int(self):
        data = [1, 2, 3, 4, 5]
        result = _sum(data)
        self.assertEqual(result, 15)

    def test_list_float(self):
        data = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = _sum(data)
        self.assertEqual(result, 16.5)

    def test_empty_list(self):
        data = []
        result = _sum(data)
        self.assertEqual(result, 0)

    def test_single_element(self):
        data = [10]
        result = _sum(data)
        self.assertEqual(result, 10)

    def test_negative_numbers(self):
        data = [-1, -2, -3, -4, -5]
        result = _sum(data)
        self.assertEqual(result, -15)

    def test_mixed_numbers(self):
        data = [-1, 2, -3, 4, -5]
        result = _sum(data)
        self.assertEqual(result, -3)

    def test_string_input(self):
        data = ['1', '2', '3', '4', '5']
        with self.assertRaises(TypeError):
            _sum(data)

    def test_non_iterable_input(self):
        data = 12345
        with self.assertRaises(TypeError):
            _sum(data)
