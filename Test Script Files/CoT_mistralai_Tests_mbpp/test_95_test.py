import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['a']), 1)

    def test_multiple_elements_same_length(self):
        self.assertEqual(Find_Min_Length(['aa', 'bb', 'cc']), 2)

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(Find_Min_Length(['aa', 'ab', 'a']), 1)

    def test_negative_strings(self):
        self.assertEqual(Find_Min_Length(['-a', '-b', '-c']), 1)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            Find_Min_Length([1, 2, 'a'])

    def test_empty_string(self):
        self.assertEqual(Find_Min_Length(['', 'a']), 1)
