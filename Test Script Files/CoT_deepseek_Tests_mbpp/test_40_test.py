import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        expected_output = {1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
        self.assertEqual(freq_element(nums), expected_output)

    def test_empty_list(self):
        nums = []
        expected_output = {}
        self.assertEqual(freq_element(nums), expected_output)

    def test_single_list(self):
        nums = [[1, 2, 3]]
        expected_output = {1: 1, 2: 1, 3: 1}
        self.assertEqual(freq_element(nums), expected_output)

    def test_single_element(self):
        nums = [[1]]
        expected_output = {1: 1}
        self.assertEqual(freq_element(nums), expected_output)

    def test_duplicate_elements(self):
        nums = [[1, 1, 2, 2], [2, 2, 3, 3]]
        expected_output = {1: 2, 2: 4, 3: 2}
        self.assertEqual(freq_element(nums), expected_output)

    def test_empty_sublists(self):
        nums = [[]]
        expected_output = {}
        self.assertEqual(freq_element(nums), expected_output)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            freq_element(None)
