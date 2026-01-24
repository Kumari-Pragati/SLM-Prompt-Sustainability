import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_single_list(self):
        self.assertEqual(freq_element([[1, 2, 3]]), {1: 1, 2: 1, 3: 1})

    def test_multiple_lists(self):
        self.assertEqual(freq_element([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {1: 1, 2: 2, 3: 2, 4: 2, 5: 1})

    def test_empty_list(self):
        self.assertEqual(freq_element([]), {})

    def test_empty_input(self):
        self.assertEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertEqual(freq_element([[1]]), {1: 1})

    def test_duplicates(self):
        self.assertEqual(freq_element([[1, 1, 2, 2, 3, 3]]), {1: 2, 2: 2, 3: 2})

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            freq_element([[1, 2, 'a', 'b', 3, 4]])
