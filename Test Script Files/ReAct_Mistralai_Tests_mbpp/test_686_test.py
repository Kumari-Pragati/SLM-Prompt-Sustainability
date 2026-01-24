import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_element([]), "{}")

    def test_single_element(self):
        self.assertEqual(freq_element([1]), "{'1': 1}")

    def test_multiple_elements(self):
        self.assertEqual(freq_element([1, 1, 2, 2, 3]), "{'1': 2, '2': 2, '3': 1}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element([1, 1, 2, 2, 2, 3]), "{'1': 3, '2': 3, '3': 1}")

    def test_negative_numbers(self):
        self.assertEqual(freq_element([1, -1, 1, -1]), "{'1': 2, '-1': 2}")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            freq_element([1, "a", 2])

    def test_large_input(self):
        large_list = [i for i in range(1000)]
        self.assertEqual(freq_element(large_list), f"{{{', '.join(str(k) + ': ' + str(v) for k, v in sorted(freq_element(large_list).items())))}}")
