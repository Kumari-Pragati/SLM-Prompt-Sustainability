import unittest
from mbpp_305_code import start_withp

class TestStartsWithP(unittest.TestCase):

    def test_start_withp(self):
        self.assertEqual(start_withp(["Panda loves Pingu"]), (('Panda', 'Pingu'),))
        self.assertEqual(start_withp(["Panda", "Pingu"]), None)
        self.assertEqual(start_withp(["Panda loves Pingu", "Pingu loves Panda"]), (('Panda', 'Pingu'), ('Pingu', 'Panda')))
        self.assertEqual(start_withp([]), None)
