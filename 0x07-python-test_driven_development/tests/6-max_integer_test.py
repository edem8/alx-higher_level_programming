#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Testing the max_integer function imported """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_exception(self):
        self.assertRaises(TypeError, max_integer, 3)

    def test_list_element(self):
        self.assertRaises(TypeError, max_integer, ["3", 4, 6])

    def test_no_list_passed(self):
        self.assertEqual(max_integer(), None)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([6, 3, 2]), 6)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([2, 5, 1]), 5)

    def test_negative_number(self):
        self.assertEqual(max_integer([2, -4, 0]), 2)

    def test_only_negative_list(self):
        self.assertEqual(max_integer([-3, -1, -7]), -1)

    def test_one_element_list(self):
        self.assertEqual(max_integer([4]), 4)

