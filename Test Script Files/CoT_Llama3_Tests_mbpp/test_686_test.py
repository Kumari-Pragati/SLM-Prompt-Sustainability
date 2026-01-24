import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(freq_element(()), '({})')

    def test_single_element(self):
        self.assertEqual(freq_element((1,)), '(1:)')

    def test_multiple_elements(self):
        self.assertEqual(freq_element((1, 2, 2, 3, 3, 3)), '(1:1, 2:2, 3:3)')

    def test_duplicates(self):
        self.assertEqual(freq_element((1, 1, 2, 2, 2, 3)), '(1:2, 2:3, 3:1)')

    def test_non_integer_elements(self):
        self.assertEqual(freq_element(("a", "b", "b", "c")), '({"a":1, "b":2, "c":1})')

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            freq_element(None)

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            freq_element("")
