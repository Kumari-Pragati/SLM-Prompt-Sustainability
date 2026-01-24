import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_typical_use_case(self):
        input_list = [1, 2, 3, 4, 5]
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)

    def test_empty_list(self):
        input_list = []
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)

    def test_single_element_list(self):
        input_list = [1]
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)

    def test_large_list(self):
        input_list = list(range(1, 1001))
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)

    def test_list_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)

    def test_list_with_negative_numbers(self):
        input_list = [-1, -2, -3, -4, -5]
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)

    def test_list_with_mixed_numbers(self):
        input_list = [-1, 0, 1, 2, 3]
        output_list = lcopy(input_list)
        self.assertEqual(input_list, output_list)
        self.assertIsNot(input_list, output_list)
