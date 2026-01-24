import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsInstance(extract_min_max((), K=0), tuple)
        self.assertIsInstance(extract_min_max((), K=1), tuple)

    def test_single_element(self):
        self.assertIsInstance(extract_min_max((1,), K=0), tuple)
        self.assertIsInstance(extract_min_max((1,), K=1), tuple)

    def test_two_elements(self):
        self.assertIsInstance(extract_min_max((1, 2), K=0), tuple)
        self.assertIsInstance(extract_min_max((1, 2), K=1), tuple)

    def test_min_and_max_at_boundaries(self):
        self.assertIsInstance(extract_min_max((min_val, values, max_val), K=1), tuple)
        self.assertIsInstance(extract_min_max((min_val, values, max_val), K=2), tuple)

    def test_min_and_max_in_middle(self):
        self.assertIsInstance(extract_min_max((min_val, values, max_val), K=0), tuple)
        self.assertIsInstance(extract_min_max((min_val, values, max_val), K=len(values) // 2), tuple)

    def test_negative_values(self):
        self.assertIsInstance(extract_min_max((-1, 0, 1), K=1), tuple)
        self.assertIsInstance(extract_min_max((-1, 0, 1), K=2), tuple)

    def test_duplicate_values(self):
        self.assertIsInstance(extract_min_max((1, 1, 2), K=1), tuple)
        self.assertIsInstance(extract_min_max((1, 1, 2), K=2), tuple)
