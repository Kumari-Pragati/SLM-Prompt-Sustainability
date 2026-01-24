import unittest
from mbpp_928_code import datetime, timedelta
from dateutil.relativedelta import relativedelta

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_cases(self):
        test_cases = [
            ('2022-01-01', '01-01-2022'),
            ('2022-12-31', '31-12-2022'),
            ('2022-02-29', '29-02-2022'),  # Leap year
            ('2021-12-31', '31-12-2021'),
            ('2020-02-29', '29-02-2020'),  # Non-leap year
        ]
        for input_, expected in test_cases:
            self.assertEqual(change_date_format(input_), expected)

    def test_edge_and_boundary_cases(self):
        test_cases = [
            ('0001-01-01', '01-01-0001'),
            ('9999-12-31', '31-12-9999'),
            ('2022-01-01T00:00:00', '01-01-2022'),  # Timestamp
            ('2022-12-31T23:59:59', '31-12-2022'),  # Timestamp
            ('2022-02-29T23:59:59', '29-02-2022'),  # Timestamp
            ('2022-02-29T00:00:00', '29-02-2022'),  # Timestamp
            ('2022-02-29-00:00', '29-02-2022'),  # Mixed format
            ('2022-02-29 00:00', '29-02-2022'),  # Mixed format
            ('2022-02-29 23:59:59', '29-02-2022'),  # Mixed format
            ('2022-02-29Z', '29-02-2022'),  # ISO format
            ('2022-02-29+00:00', '29-02-2022'),  # ISO format with timezone
            ('2022-02-29-00:00Z', '29-02-2022'),  # Mixed format with ISO timezone
            ('2022-02-29-00:00+00:00', '29-02-2022'),  # Mixed format with ISO timezone
        ]
        for input_, expected in test_cases:
            self.assertEqual(change_date_format(input_), expected)

    def test_invalid_inputs(self):
        test_cases = [
            ('', ''),
            ('abc', ''),
            ('2022', '22-00-0000'),
            ('2022-13', '13-00-0000'),
            ('2022-01-32', '01-32-0000'),
            ('2022-02-29-30', '29-30-0000'),
            ('2022-02-29 30:00', '29-30-0000'),
            ('2022-02-29T30:00', '29-30-0000'),
            ('2022-02-29Z30', '29-30-0000'),
            ('2022-02-29+00:30', '29-00-0000