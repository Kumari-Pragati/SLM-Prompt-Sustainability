import unittest
from mbpp_898_code import groupby

def extract_elements(numbers, n):
    result = [i for i, j in groupby(numbers) if len(list(j)) == n]
    return result

class TestExtractElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_elements([], 1), [])

    def test_single_element(self):
        self.assertListEqual(extract_elements([1], 1), [1])
        self.assertListEqual(extract_elements([1], 2), [])

    def test_single_element_group(self):
        self.assertListEqual(extract_elements([1, 1], 1), [1])
        self.assertListEqual(extract_elements([1, 1], 2), [])

    def test_multiple_elements(self):
        self.assertListEqual(extract_elements([1, 2, 3, 4, 5], 2), [(2, 3), (4, 5)])

    def test_multiple_element_groups(self):
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2),
                             [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
