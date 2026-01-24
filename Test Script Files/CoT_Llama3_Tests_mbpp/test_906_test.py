import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):
    def test_typical_input(self):
        url = 'https://example.com/2022/07/25/'
        self.assertEqual(extract_date(url), [('2022', '07', '25')])

    def test_edge_case_1(self):
        url = 'https://example.com/2022/07/25'
        self.assertEqual(extract_date(url), [])

    def test_edge_case_2(self):
        url = 'https://example.com/2022/07'
        self.assertEqual(extract_date(url), [])

    def test_edge_case_3(self):
        url = 'https://example.com/2022'
        self.assertEqual(extract_date(url), [])

    def test_invalid_input_1(self):
        url = 'https://example.com/invalid'
        self.assertEqual(extract_date(url), [])

    def test_invalid_input_2(self):
        url = 'https://example.com'
        self.assertEqual(extract_date(url), [])

    def test_invalid_input_3(self):
        url = 'invalid url'
        with self.assertRaises(TypeError):
            extract_date(url)
