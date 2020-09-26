#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def testMax(self):
        self.assertEqual(max_integer([-10, -6, -2]), -2)
        self.assertEqual(max_integer([4, 5, 10, 50, 60]), 60)
        self.assertEqual(max_integer([100, 5, 10, 50]), 100)
        self.assertEqual(max_integer('Holberton'), 't')
        self.assertEqual(max_integer([-10, -6, 0]), 0)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
