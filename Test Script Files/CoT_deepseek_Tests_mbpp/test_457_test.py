import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_single_element(self):
        self.assertEqual(Find_Min([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Min([])

    def test_non_integer_elements(self):
        self.assertEqual(Find_Min([1.1, 1.2, 1.3, 1.4, 1.5]), 1.1)

    def test_mixed_integer_float(self):
        self.assertEqual(Find_Min([1, 2.2, 3, 4.4, 5]), 1)

    def test_duplicates(self):
        self.assertEqual(Find_Min([1, 1, 2, 3, 4]), 1)

    def test_large_numbers(self):
        self.assertEqual(Find_Min([1000000000, 2000000000, 3000000000, 4000000000, 5000000000]), 1000000000)
