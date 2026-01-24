import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):

    def test_start_withp(self):
        self.assertEqual(start_withp(['Pete is a programmer']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot']), ('Pete', 'programmer'))
        self.assertEqual(start_withp(['Pete is a programmer, Paul is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot, Peter is a pilot,