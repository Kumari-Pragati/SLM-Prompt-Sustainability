import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_single_element_list(self):
        self.assertEqual(Find_Min([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -5)

    def test_duplicate_elements(self):
        self.assertEqual(Find_Min([2, 2, 2, 2, 2]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(Find_Min([-1, 2, 0, 3, -5]), -5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Find_Min("not a list")
