import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
        expected_result = {1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 1, 7: 1}
        self.assertEqual(freq_element(nums), expected_result)

    def test_empty_list(self):
        nums = []
        expected_result = {}
        self.assertEqual(freq_element(nums), expected_result)

    def test_single_list(self):
        nums = [[1, 2, 3]]
        expected_result = {1: 1, 2: 1, 3: 1}
        self.assertEqual(freq_element(nums), expected_result)

    def test_duplicate_elements(self):
        nums = [[1, 1, 2], [2, 2, 3]]
        expected_result = {1: 2, 2: 2, 3: 1}
        self.assertEqual(freq_element(nums), expected_result)

    def test_empty_sublists(self):
        nums = [[]]
        expected_result = {}
        self.assertEqual(freq_element(nums), expected_result)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            freq_element("not a list")
