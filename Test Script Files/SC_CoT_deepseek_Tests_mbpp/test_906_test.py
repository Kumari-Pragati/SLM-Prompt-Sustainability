import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):
    
    def test_typical_case(self):
        url = 'https://www.example.com/2022/01/01/'
        self.assertEqual(extract_date(url), [('2022', '01', '01')])

    def test_edge_cases(self):
        url = 'https://www.example.com/2000/01/01/'
        self.assertEqual(extract_date(url), [('2000', '01', '01')])

        url = 'https://www.example.com/2022/12/31/'
        self.assertEqual(extract_date(url), [('2022', '12', '31')])

    def test_corner_cases(self):
        url = 'https://www.example.com/2022/02/28/'
        self.assertEqual(extract_date(url), [('2022', '02', '28')])

        url = 'https://www.example.com/2022/02/29/'
        self.assertEqual(extract_date(url), [])

    def test_invalid_inputs(self):
        url = 'https://www.example.com/2022/13/01/'
        self.assertEqual(extract_date(url), [])

        url = 'https://www.example.com/2022/01/32/'
        self.assertEqual(extract_date(url), [])

        url = 'https://www.example.com/2022/01/01/extra'
        self.assertEqual(extract_date(url), [])
