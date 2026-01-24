import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_single_element_list(self):
        self.assertEqual(Find_Min([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_min_value_at_beginning(self):
        self.assertEqual(Find_Min([0, 1, 2, 3, 4]), 0)

    def test_min_value_in_middle(self):
        self.assertEqual(Find_Min([1, 0, 2, 3, 4]), 0)

    def test_min_value_at_end(self):
        self.assertEqual(Find_Min([1, 2, 3, 0, 4]), 0)

    def test_min_value_negative_numbers(self):
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -1)

    def test_min_value_floats(self):
        self.assertAlmostEqual(Find_Min([1.1, 2.2, 3.3, 4.4, 5.5]), 1.1)

    def test_min_value_mixed_types(self):
        self.assertEqual(Find_Min([1, 2, 3, 'a', 0]), 0)

    def test_min_value_duplicates(self):
        self.assertEqual(Find_Min([1, 1, 2, 3, 4]), 1)

    def test_min_value_no_min(self):
        self.assertIsNone(Find_Min([1, 2, 3]))
