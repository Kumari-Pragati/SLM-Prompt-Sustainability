import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(freq_element(('a', 'b', 'c', 'a', 'b')), "{'a': 2, 'b': 2, 'c': 1}")

    def test_edge_condition(self):
        self.assertEqual(freq_element(()), "{}")

    def test_boundary_condition(self):
        self.assertEqual(freq_element(('a',)), "{'a': 1}")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            freq_element(123)
