import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_simple_date_format(self):
        self.assertListEqual(extract_date('/2022/01/01/'), [('2022', '01', '01')])
        self.assertListEqual(extract_date('/2022/01/31/'), [('2022', '01', '31')])
        self.assertListEqual(extract_date('/2022/12/31/'), [('2022', '12', '31')])

    def test_edge_cases(self):
        self.assertListEqual(extract_date('/2022/01/00/'), [])
        self.assertListEqual(extract_date('/2022/13/01/'), [])
        self.assertListEqual(extract_date('/2022/01/32/'), [])
        self.assertListEqual(extract_date('/2022/00/01/'), [])
        self.assertListEqual(extract_date('/2022/12/32/'), [])

    def test_complex_date_formats(self):
        self.assertListEqual(extract_date('/2022/01/01/01/'), [])
        self.assertListEqual(extract_date('/2022/01/01/2022/'), [])
        self.assertListEqual(extract_date('/2022/01/01/2022/01/'), [])
        self.assertListEqual(extract_date('/2022/01/01/2022/01/01/'), [])
