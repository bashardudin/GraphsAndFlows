# -*- coding: utf-8 -*-
"""Stack test module."""

from collections import deque

from ..stack import Stack

import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.bag = Stack()

    def test_init(self):
        """Test empty stack init."""

        self.assertEqual(deque, type(self.bag.elements))

    def test_isempty(self):
        """Test new stack emptyness."""

        self.assertTrue(self.bag.isempty())

    def test_push(self):
        """Test pushing elements."""

        self.bag = self.bag.push(0)
        self.assertEqual(1, len(self.bag.elements))
        self.assertEqual(0, self.bag.elements[0])
        self.bag = self.bag.push(1)
        self.assertEqual(2, len(self.bag.elements))
        self.assertEqual(1, self.bag.elements[1])

    def test_pop(self):
        """Test dequeuing elements."""

        values = [ 0, 1, 2 ]
        for val in values:
            self.bag.elements.append(val)
        for i in range(len(values) - 1, -1, -1):
            self.assertEqual(values[i], self.bag.pop())
        self.assertEqual(0, len(self.bag.elements))

    def test_top(self):
        """Test peeking at top element."""

        values = [ 0, 1, 2 ]
        for val in values:
            self.bag.elements.append(val)
        self.assertEqual(values[-1], self.bag.top())
        self.bag.elements.pop()
        self.assertEqual(values[-2], self.bag.top())


if __name__ == '__main__':
    unittest.main()
