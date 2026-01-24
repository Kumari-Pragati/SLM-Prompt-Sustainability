import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(sum_elements(()), 0)

    def test_single_element(self):
        self.assertEqual(sum_elements((1,)), 1)

    def test_multiple_elements(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3)), 2)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sum_elements((1, "two", 3))

    def test_list_as_input(self):
        with self.assertRaises(TypeError):
            sum_elements([1, 2, 3])

    def test_tuple_with_none(self):
        self.assertEqual(sum_elements((1, None, 3)), 4)
