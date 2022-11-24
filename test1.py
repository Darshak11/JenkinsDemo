import unittest
from long_palin_sub_seq import lps

class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(lps("abbab",0,len("abbab")-1), 4)

    def testCase2(self):
        self.assertEqual(lps("abaaba",0,len("abaaba")-1), 6)

    def testCase3(self):
        self.assertEqual(lps("cbbd",0,len("cbbd")-1), 2)

if __name__ == '__main__':
    unittest.main()