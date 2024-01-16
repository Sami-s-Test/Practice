import unittest
from cigar_party import cigar_party

class TestCigarParty(unittest.TestCase):

    def test_less_than_40_is_weekend(self):
        self.assertEqual(cigar_party(20, True), False)

    def test_less_than_40_not_is_weekend(self):
        self.assertEqual(cigar_party(20, False), False)

    def test_40_is_weekend(self):
        self.assertEqual(cigar_party(40, True), True)

    def test_40_not_is_weekend(self):
        self.assertEqual(cigar_party(40, False), True)

    def test_48_is_weekend(self):
        self.assertEqual(cigar_party(48, True), True)

    def test_48_not_is_weekend(self):
        self.assertEqual(cigar_party(48, False), True)

    def test_60_is_weekend(self):
        self.assertEqual(cigar_party(60, True), True)

    def test_60_not_is_weekend(self):
        self.assertEqual(cigar_party(60, False), True)

    def test_72_is_weekend(self):
        self.assertEqual(cigar_party(72, True), True)

    def test_72_not_is_weekend(self):
        self.assertEqual(cigar_party(72, False), False)

if __name__ == '__main__':
    unittest.main()