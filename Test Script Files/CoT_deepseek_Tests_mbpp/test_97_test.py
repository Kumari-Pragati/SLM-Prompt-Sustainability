import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [2, 3, 4]]), {1: 1, 2: 2, 3: 2, 4: 1})

    def test_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_single_element(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_duplicate_elements(self):
        self.assertEqual(frequency_lists([[1, 1, 1], [2, 2, 2]]), {1: 3, 2: 3})

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            frequency_lists([[1, 'a'], [2, 'b']])

    def test_nested_empty_list(self):
        self.assertEqual(frequency_lists([[]]), {})

    def test_nested_list_with_none(self):
        self.assertEqual(frequency_lists([[None]]), {None: 1})
