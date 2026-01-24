import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_simple_url(self):
        self.assertEqual(extract_date('/2023/01/01/'), [('2023', '01', '01')])

    def test_edge_conditions(self):
        self.assertEqual(extract_date('/2000/01/01/'), [('2000', '01', '01')])
        self.assertEqual(extract_date('/2023/12/31/'), [('2023', '12', '31')])
        self.assertEqual(extract_date('/2023/01/01/'), [('2023', '01', '01')])
        self.assertEqual(extract_date('/2023/02/28/'), [('2023', '02', '28')])

    def test_complex_scenarios(self):
        self.assertEqual(extract_date('/2023/02/29/'), [('2023', '02', '29')])  # Leap year
        self.assertEqual(extract_date('/2023/03/31/'), [])  # Invalid date
        self.assertEqual(extract_date('/2023/13/01/'), [])  # Invalid month
        self.assertEqual(extract_date('/2023/01/32/'), [])  # Invalid day

    def test_invalid_inputs(self):
        self.assertEqual(extract_date(''), [])
        self.assertEqual(extract_date('/'), [])
        self.assertEqual(extract_date('2023/01/01/'), [])
        self.assertEqual(extract_date('/2023/01/01'), [])
