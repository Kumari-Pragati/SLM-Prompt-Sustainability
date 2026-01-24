import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_min_length(self):
        self.assertEqual(min_length(['abc', 'de', 'fghi']), (2, 'de'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'j']), (1, 'j'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmn']), (1, 'jklmn'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnop']), (1, 'jklmnop'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopq']), (1, 'jklmnopq'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqr']), (1, 'jklmnopqr'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrs']), (1, 'jklmnopqrs'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrst']), (1, 'jklmnopqrst'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrstu']), (1, 'jklmnopqrstu'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrstuv']), (1, 'jklmnopqrstuv'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrstuvw']), (1, 'jklmnopqrstuvw'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrstuvwx']), (1, 'jklmnopqrstuvwx'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrstuvwxy']), (1, 'jklmnopqrstuvwxy'))
        self.assertEqual(min_length(['abc', 'de', 'fghi', 'jklmnopqrstuvwxyz']), (1, 'jklmnopqrstuvwxyz'))
