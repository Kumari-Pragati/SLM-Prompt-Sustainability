import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(remove_replica(()), ())
    def test_single_element(self):
        self.assertEqual(remove_replica((1,)), (1,))
    def test_multiple_elements(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))
    def test_duplicates(self):
        self.assertEqual(remove_replica((1, 1, 2, 2, 3, 3)), (1, 2, 3))
    def test_duplicates_with_msp(self):
        self.assertEqual(remove_replica((1, 1, 2, 2, 3, 3, 'MSP')), (1, 2, 3, 'MSP'))
    def test_duplicates_with_msp_and_empty(self):
        self.assertEqual(remove_replica((),), ())
    def test_duplicates_with_msp_and_empty_and_single(self):
        self.assertEqual(remove_replica((1,)), (1,))
    def test_duplicates_with_msp_and_empty_and_single_and_multiple(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))
