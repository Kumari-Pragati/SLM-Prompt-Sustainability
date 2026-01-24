import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(freq_element([[1, 2, 3], [2, 3, 4]]), {1: 1, 2: 2, 3: 2, 4: 1})

    def test_empty_list(self):
        self.assertEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertEqual(freq_element([[1]]), {1: 1})

    def test_duplicate_elements(self):
        self.assertEqual(freq_element([[1, 1, 2, 2], [2, 2, 3, 3]]), {1: 2, 2: 4, 3: 2})

    def test_single_sublist(self):
        self.assertEqual(freq_element([[1, 2, 3]]), {1: 1, 2: 1, 3: 1})

    def test_empty_sublists(self):
        self.assertEqual(freq_element([[], []]), {})

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            freq_element([[1, 'a'], [2, 'b']])
