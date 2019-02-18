# -*- coding: utf-8 -*-
"""Stack module."""

from collections import deque

class Stack:
    """Simple class for LIFO (last-in-first-out) container."""

    def __init__(self):
        """Init stack."""

        self.elements = deque()

    def push(self, elt):
        """Add an element to the stack.

        Args:
                elt (Any): Element to push.

        Returns:
            Stack: The updated stack.

        """

        self.elements.append(elt)
        return self

    def peek(self):
        """Return top element without modifying the stack.

        Returns:
            Any: Top element from stack.
        """

        return self.elements[len(self.elements)-1]

    def pop(self):
        """Remove and return next element from the stack.

        Returns:
            Any: Element from stack.
        """

        return self.elements.pop()

    def isempty(self):
        """Check whether stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise.

        """

        return len(self.elements) == 0
