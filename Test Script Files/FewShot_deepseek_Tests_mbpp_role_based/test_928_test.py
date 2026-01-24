import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case(self):
        self.assertEqual(change_date_format('2000-02-29'), '29-02-2000')

    def test_boundary_case(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            change_date_format('2022-13-01')
