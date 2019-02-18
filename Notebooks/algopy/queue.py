# -*- coding: utf-8 -*-
"""Queue module."""

from collections import deque

class Queue:
    """Simple class for FIFO (first-in-first-out) container."""

    def __init__(self):
        """Init queue."""

        self.elements = deque()

    def enqueue(self, elt):
        """Add an element to the queue.

        Args:
            elt (Any): Element to enqueue.

        Returns:
            Queue: The updated queue.

        """

        self.elements.append(elt)
        return self

    def dequeue(self):
        """Remove and return next element from the queue.

        Returns:
            Any: Element from the queue.

        Raises:
            IndexError: If queue is empty.

        """

        return self.elements.popleft()

    def isempty(self):
        """Check whether queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.

        """

        return len(self.elements) == 0
