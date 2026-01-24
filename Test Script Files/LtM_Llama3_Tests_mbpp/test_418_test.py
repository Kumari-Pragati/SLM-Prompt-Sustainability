import unittest
from mbpp_418_code import Find_Max

class TestFind_Max(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_empty_input(self):
        self.assertRaises(ValueError, Find_Max, [])

    def test_single_element_input(self):
        self.assertEqual(Find_Max([10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(Find_Max([-5, -3, -1, 0, 2]), 2)

    def test_multiple_max_values(self):
        self.assertEqual(Find_Max([1, 2, 2, 3, 4, 5]), 5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Find_Max(['a', 'b', 'c'])
