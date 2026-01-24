import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_typical_case(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, sorted(subjectmarks, key=lambda x: x[1]))

    def test_edge_case(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_edge_case2(self):
        subjectmarks = [('English', 88), ('Maths', 97), ('Science', 90)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_edge_case3(self):
        subjectmarks = [('Maths', 97), ('Science', 90), ('English', 88)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_empty_input(self):
        subjectmarks = []
        result = subject_marks(subjectmarks)
        self.assertEqual(result, [])

    def test_single_input(self):
        subjectmarks = [('English', 88)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            subject_marks('Invalid input')
