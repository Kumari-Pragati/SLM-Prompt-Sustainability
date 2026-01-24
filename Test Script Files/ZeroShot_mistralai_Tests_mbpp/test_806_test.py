import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_all_uppercase(self):
        self.assertEqual(max_run_uppercase("HELLO"), 5)

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase("HeLlO wOrLd"), 3)

    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase("aBc"), 1)

    def test_multiple_runs(self):
        self.assertEqual(max_run_uppercase("HELLOWORLD"), 5)

    def test_long_string(self):
        long_string = "".join([chr(i) for i in range(ord('A'), ord('Z') + 1)]) + "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
        self.assertEqual(max_run_uppercase(long_string), len(long_string) // 26)
