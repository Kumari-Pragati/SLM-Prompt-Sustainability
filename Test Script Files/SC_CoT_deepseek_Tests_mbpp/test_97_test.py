import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [2, 3, 4]]), {1: 1, 2: 2, 3: 2, 4: 1})

    def test_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_single_item_list(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_single_sublist(self):
        self.assertEqual(frequency_lists([[1, 2, 3]]), {1: 1, 2: 1, 3: 1})

    def test_duplicate_items(self):
        self.assertEqual(frequency_lists([[1, 1, 2, 2], [2, 2, 3, 3]]), {1: 2, 2: 4, 3: 2})

    def test_negative_numbers(self):
        self.assertEqual(frequency_lists([[-1, -2, -2], [-2, -3, -3]]), {-1: 1, -2: 2, -3: 2})

    def test_mixed_numbers(self):
        self.assertEqual(frequency_lists([[1, -1, 2, -2], [-1, -2, 2, 2]]), {1: 1, -1: 2, 2: 2, -2: 2})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            frequency_lists(123)
