import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(extract_max("1 2 3 4 5"), 5)
        self.assertEqual(extract_max("100 200 300 400 500"), 500)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(extract_max(""), 0)
        self.assertEqual(extract_max("1"), 1)
        self.assertEqual(extract_max("1234567890"), 90)
        self.assertEqual(extract_max("12345678901"), 90)
        self.assertEqual(extract_max("123456789012"), 12)
        self.assertEqual(extract_max("1234567890123"), 123)

    def test_special_cases(self):
        self.assertEqual(extract_max("1a2b3c"), 1)
        self.assertEqual(extract_max("1_2_3_4_5"), 5)
        self.assertEqual(extract_max("1+2*3-4/5"), 5)
        self.assertEqual(extract_max("1-2-3-4-5"), -5)
        self.assertEqual(extract_max("1e2e3e4e5"), 1)
        self.assertEqual(extract_max("1E2E3E4E5"), 1)
        self.assertEqual(extract_max("1.2.3.4.5"), 5)
