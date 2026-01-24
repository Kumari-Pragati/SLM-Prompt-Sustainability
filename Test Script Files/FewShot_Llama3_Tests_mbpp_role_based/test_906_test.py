import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):
    def test_valid_url(self):
        url = "https://example.com/2022/07/25/"
        self.assertEqual(extract_date(url), [("2022", "07", "25")])

    def test_valid_url_with_trailing_slash(self):
        url = "https://example.com/2022/07/25/"
        self.assertEqual(extract_date(url), [("2022", "07", "25")])

    def test_invalid_url(self):
        url = "https://example.com/invalid"
        self.assertEqual(extract_date(url), [])

    def test_url_without_date(self):
        url = "https://example.com/no-date"
        self.assertEqual(extract_date(url), [])

    def test_url_with_multiple_dates(self):
        url = "https://example.com/2022/07/25/2023/08/26/"
        self.assertEqual(extract_date(url), [("2022", "07", "25"), ("2023", "08", "26")])
