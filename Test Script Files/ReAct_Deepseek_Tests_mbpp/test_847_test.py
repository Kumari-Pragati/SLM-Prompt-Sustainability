import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):

    def test_typical_case(self):
        input_list = [1, 2, 3, 4, 5]
        output_list = lcopy(input_list)
        self.assertEqual(output_list, input_list)
        self.assertIsNot(output_list, input_list)

    def test_empty_list(self):
        input_list = []
        output_list = lcopy(input_list)
        self.assertEqual(output_list, input_list)
        self.assertIsNot(output_list, input_list)

    def test_single_element_list(self):
        input_list = [1]
        output_list = lcopy(input_list)
        self.assertEqual(output_list, input_list)
        self.assertIsNot(output_list, input_list)

    def test_large_list(self):
        input_list = list(range(1, 1001))
        output_list = lcopy(input_list)
        self.assertEqual(output_list, input_list)
        self.assertIsNot(output_list, input_list)

    def test_list_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        output_list = lcopy(input_list)
        self.assertEqual(output_list, input_list)
        self.assertIsNot(output_list, input_list)

    def test_list_with_none_elements(self):
        input_list = [1, None, 3, 4, None, 5]
        output_list = lcopy(input_list)
        self.assertEqual(output_list, input_list)
        self.assertIsNot(output_list, input_list)
