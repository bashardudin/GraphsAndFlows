# -*- coding: utf-8 -*-
"""Queue test module."""

from collections import deque

from ..queue import Queue

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.bag = Queue()

    def test_init(self):
        """Test empty queue init."""

        self.assertEqual(deque, type(self.bag.elements))

    def test_isempty(self):
        """Test new queue emptyness."""

        self.assertTrue(self.bag.isempty())

    def test_enqueue(self):
        """Test enqueuing elements."""

        self.bag = self.bag.enqueue(0)
        self.assertEqual(1, len(self.bag.elements))
        self.assertEqual(0, self.bag.elements[0])
        self.bag = self.bag.enqueue(1)
        self.assertEqual(2, len(self.bag.elements))
        self.assertEqual(1, self.bag.elements[1])

    def test_dequeue(self):
        """Test dequeuing elements."""

        values = [ 0, 1, 2 ]
        for val in values:
            self.bag.elements.append(val)
        for val in values:
            self.assertEqual(val, self.bag.dequeue())
        self.assertEqual(0, len(self.bag.elements))

if __name__ == '__main__':
    unittest.main()
