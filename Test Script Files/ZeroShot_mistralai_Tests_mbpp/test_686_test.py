import unittest
from mbpp_686_code import defaultdict
from typing import Tuple

from 686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_element([]), "{}")

    def test_single_element(self):
        self.assertEqual(freq_element(("a",)), "{'a': 1}")

    def test_multiple_elements(self):
        self.assertEqual(freq_element(("a", "b", "a", "c", "b", "a")), "{'a': 3, 'b': 2, 'c': 1}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element(("a", "a", "a", "b", "b", "b")), "{'a': 3, 'b': 3}")

    def test_mixed_case_elements(self):
        self.assertEqual(freq_element(("A", "a", "B", "b")), "{'A': 1, 'a': 1, 'B': 1, 'b': 1}")

    def test_non_string_elements(self):
        self.assertRaises(TypeError, freq_element, (1, 2, 3))
