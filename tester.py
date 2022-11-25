#!/usr/bin/python3

import unittest
from prob1 import OddEven
from prob2 import pred

class Calculator(unittest.TestCase):

    def test_OddEven(self):
        x = 3
        res = OddEven(x)
        self.assertEqual(res, 6)

    def test_pred(self):
        x = 99
        res1 = pred(x)
        self.assertEqual(res1, 98)
    
    def test_pred(self):
        x = 99
        res1 = pred(x)
        self.assertEqual(res1, 97)
    

if __name__ == '__main__':
    unittest.main()
