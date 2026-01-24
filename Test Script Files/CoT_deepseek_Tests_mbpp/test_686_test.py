import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(freq_element(('a', 'b', 'c', 'a', 'b', 'b')), "{'a': 2, 'b': 3, 'c': 1}")

    def test_single_element(self):
        self.assertEqual(freq_element(('a',)), "{'a': 1}")

    def test_empty_tuple(self):
        self.assertEqual(freq_element(()), "{}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element(('a', 'a', 'a', 'b', 'b', 'c')), "{'a': 3, 'b': 2, 'c': 1}")

    def test_large_tuple(self):
        test_tup = tuple('a' for _ in range(1000))
        self.assertEqual(freq_element(test_tup), "{'a': 1000}")

    def test_mixed_case(self):
        self.assertEqual(freq_element(('a', 'B', 'c', 'a', 'B', 'B')), "{'a': 2, 'B': 3, 'c': 1}")

    def test_numeric_elements(self):
        self.assertEqual(freq_element((1, 2, 3, 1, 2, 2)), "{1: 2, 2: 3, 3: 1}")

    def test_none_elements(self):
        with self.assertRaises(TypeError):
            freq_element((None, None))
