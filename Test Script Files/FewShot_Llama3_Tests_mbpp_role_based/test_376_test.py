import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))

    def test_duplicates(self):
        self.assertEqual(remove_replica((1, 2, 2, 3, 1)), (1, 2, 3))

    def test_duplicates_with_msp(self):
        self.assertEqual(remove_replica((1, 2, 2, 3, 1, 'MSP')), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(remove_replica(()), ())

    def test_single_element(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_mixed_types(self):
        self.assertEqual(remove_replica((1, 'a', 2, 'b')), (1, 'a', 2, 'b'))

    def test_mixed_types_with_duplicates(self):
        self.assertEqual(remove_replica((1, 'a', 2, 'a', 2, 'b')), (1, 'a', 2, 'b'))
