#!/usr/bin/python3

import unittest
from prob1 import OddEven
from prob2 import pred

class Calculator(unittest.TestCase):

    def test_OddEven(self):
        x = 12
        res = OddEven(x)
        self.assertEqual(res, 24)

    def test_pred(self):
        x = 9
        res1 = pred(x)
        self.assertEqual(res1, 10)
    
    

if __name__ == '__main__':
    unittest.main()
