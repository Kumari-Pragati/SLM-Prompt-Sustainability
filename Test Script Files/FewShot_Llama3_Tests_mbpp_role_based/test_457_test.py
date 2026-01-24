import unittest
from mbpp_457_code import Find_Min

class TestFind_Min(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertRaises(ValueError, Find_Min, [])

    def test_single_element_list(self):
        self.assertEqual(Find_Min([10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(Find_Min([-5, -3, -1]), -5)

    def test_duplicates(self):
        self.assertEqual(Find_Min([1, 2, 2, 3, 4, 5]), 1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Find_Min(['a', 'b', 'c'])
