import unittest
from mbpp_906_code import datetime, timedelta
from 906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(extract_date('http://example.com/2022/01/01'), [('2022', '01', '01')])
        self.assertListEqual(extract_date('http://example.com/2022/01/31'), [('2022', '01', '31')])
        self.assertListEqual(extract_date('http://example.com/2022/12/31'), [('2022', '12', '31')])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(extract_date('http://example.com/2022/01'), [])
        self.assertListEqual(extract_date('http://example.com/2022/00'), [])
        self.assertListEqual(extract_date('http://example.com/2022/13'), [])
        self.assertListEqual(extract_date('http://example.com/2022/'), [])
        self.assertListEqual(extract_date('http://example.com/'), [])

    def test_special_cases(self):
        self.assertListEqual(extract_date('http://example.com/2022/02/29'), [('2022', '02', '29')])
        self.assertListEqual(extract_date('http://example.com/2020/02/29'), [])
        self.assertListEqual(extract_date('http://example.com/2021/02/28'), [('2021', '02', '28')])

    def test_invalid_input(self):
        self.assertListEqual(extract_date('http://example.com/a/b/c'), [])
        self.assertListEqual(extract_date('http://example.com/2022/a/b'), [])
        self.assertListEqual(extract_date('http://example.com/2022//1'), [])
        self.assertListEqual(extract_date('http://example.com/2022/1/'), [])
