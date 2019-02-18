# -*- coding: utf-8 -*-
"""General Tree module.

*Warning:* All the functions defined in this module are assumed to receive a non-None
value for their ``ref`` parameter.

Todo:
    * Save to file? Via Dot?
    * Load from file -> done!

"""

from . import queue
from .queue import Queue


class Tree:
    """Simple class for general tree.

    Attributes:
        key (Any): Node key.
        children (List[Tree]): Node children.

    """

    def __init__(self, key=None, children=None):
        """Init general tree, ensure children are properly set.

        Args:
            key (Any).
            children (List[Tree]).

        """

        self.key = key

        if children is None:
            self.children = []
        else:
            self.children = children

    @property
    def nbchildren(self):
        """Number of children of node."""

        return len(self.children)


def size(ref):
    """Compute size of tree.

    Args:
        ref (Tree).

    Returns:
        int: The number of nodes of tree.

    """

    s = 1
    for i in range(ref.nbchildren):
        s += size(ref.children[i])
    return s


def height(ref):
    """Compute height of Tree.

    Args:
        ref (Tree).

    Returns:
        int: The maximum depth of any leaf.

    """

    h = -1
    for i in range(ref.nbchildren):
        h = max(h, height(ref.children[i]))
    return h + 1


def epl(ref, h=0):
    """Compute external paths' length.

    Args:
        ref (Tree).
        h (int): Current height.

    Returns:
        int: The total length of paths from root to leaves.

    """

    if ref.nbchildren > 0:
        length = 0
        for i in range(ref.nbchildren):
            length += epl(ref.children[i], h + 1)
        return length
    else:
        return h


def search(ref, val):
    """Search for a value in tree.

    Args:
        ref (Tree).
        val (Any): Value to search.

    Returns:
        Tree: First node containing key val.

    """

    if ref.key == val:
        return ref
    else:
        for child in ref.children:
            found = search(child, val)
            if found is not None:
                return found
        return None

def __loadtree(s, typelt,i=0): 
    if i < len(s) and s[i] == '(':   # can this test be removed?
        i = i + 1 # to skip the '('
        T = Tree()
        word = ""
        while not (s[i] in "()"):
            word = word + s[i]
            i += 1
        T.key = typelt(word)
        T.children = []
        while s[i] != ')':
            (C, i) = __loadtree(s, typelt, i)
            T.children.append(C)
        i = i + 1   # to skip the ')'
        return (T, i)
    else:
        return None

def loadtree(path, typelt=int):
    # Open file and get full content
    file = open(path, 'r')
    content = file.read()
    # Remove all whitespace characters for easier parsing
    content = content.replace('\n', '').replace('\r', '') \
                     .replace('\t', '').replace(' ', '')
    file.close()
    # Parse content and return tree
    (T, _) = __loadtree(content, typelt)
    return T


def dot(ref):
    """Write down dot format of tree.

    Args:
        ref (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    s += "node [shape=circle, fixedsize=true, height=0.5, width=0.5]\n"
    q = Queue()
    q.enqueue(ref)
    while not q.isempty():
        ref = q.dequeue()
        for child in ref.children:
            s = s + "   " + str(ref.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    s += "}"
    return s


def display(ref, filename='temp'):
    """Render a tree to SVG format.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (Tree).
        filename (str): Temporary filename to store SVG output.

    Returns:
        SVG: IPython SVG wrapper object for tree.

    """

    # Ensure all modules are available
    try:
        from graphviz import Graph
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse tree and generate temporary Graph object
    output_format = 'svg'
    graph = Graph(filename, format=output_format)
    q = Queue()
    q.enqueue(ref)
    while not q.isempty():
        ref = q.dequeue()
        graph.node(str(id(ref)), label=str(ref.key))
        for child in ref.children:
            graph.edge(str(id(ref)), str(id(child)))
            q.enqueue(child)
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)
