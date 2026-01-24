import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(cummulative_sum([[1]]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4]]), 10)

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([[-1, -2], [3, 4]]), 4)

    def test_zero(self):
        self.assertEqual(cummulative_sum([[0, 0]]), 0)

    def test_max_value(self):
        self.assertEqual(cummulative_sum([[100, 100]]), 200)

    def test_min_value(self):
        self.assertEqual(cummulative_sum([[-100, -100]]), -200)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cummulative_sum("test")
