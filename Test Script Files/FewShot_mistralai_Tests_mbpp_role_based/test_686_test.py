import unittest
from mbpp_686_code import defaultdict
from six86_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(freq_element((1,)), "{'1': 1}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element((1, 1, 2)), "{'1': 2, '2': 1}")

    def test_empty_tuple(self):
        self.assertEqual(freq_element(()), "{}")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            freq_element((1, "a", [1]))
