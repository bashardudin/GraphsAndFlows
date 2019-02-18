# -*- coding: utf-8 -*-
"""Graph module.

Provide an implementation of graphs with adjacency matrix.
This can also be called static implementation.

In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. The vertex key, or number, can then be used to access its
neighbour list.

Todo:
    * Decide names for load/save: to_dot/from_dot ? save/load with format
      parameter? Specific module?
    * Add module level functions for specific tasks: build_from_list...
    * Add add_edge and add_node (and use in from_list/from_gra)
    * Handle multigraphs? (fix add_edge and dot)

"""


class GraphMat:
    """ Simple class for static graph.

    Attributes:
        order (int): Number of nodes.
        directed (bool): True if the graph is directed. False otherwise.

    """

    def __init__(self, order, directed=False, costs=False):
        self.order = order
        self.directed = directed
        self.adj = [[0 for j in range(order)] for i in range(order)]
        if costs:
            self.costs = [[float('inf') for j in range(order)] for i in range(order)]
        else:
            self.costs = None

    def addedge(self, src, dst, cost=None, multi=False):
        """Add egde to graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
            cost: if not None, the cost of edge (src, dst)
            multi (bool): True for multigraphs
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """

        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        if multi or (src != dst and self.adj[src][dst] == 0):
            self.adj[src][dst] += 1
            if not self.directed and dst != src:
                self.adj[dst][src] += 1
        if cost:
            self.costs[src][dst] = cost
            if not self.directed:
                self.costs[dst][src] = cost


    def _dot(self, engine='fdp'):
        '''Generate dot representation (as object, not source).

        Requires graphviz module.

        Returns:
            string (SVG)
        '''
        try:
            from graphviz import Graph as gvGraph, Digraph as gvDigraph
        except:
            raise Exception('Missing module: graphviz')
        g = gvDigraph(engine=engine) if self.directed else gvGraph(engine=engine)
        for src in range(self.order):
            for dst in range(self.order):
                if self.adj[src][dst] and (self.directed or src <= dst):
                    for i in range(self.adj[src][dst]):
                        g.edge(str(src), str(dst))
        return g


    def _repr_svg_(self, engine='fdp'):
        '''Generate SVG representation.

        Requires graphviz module.

        Returns:
            string (SVG)
        '''
        return self._dot(engine=engine)._repr_svg_()


    def _display(self, engine='fdp'):
        '''Displays SVG representation directly in IPython notebook.

        Requires IPython and (through method _repr_svg_) graphviz modules.
        '''
        try:
            from IPython.display import display_svg
        except:
            raise Exception('Missing moduke: IPtyhon')
        display_svg(self._dot(engine=engine))



def todot(ref):
    """Write down dot format of graph.

    Args:
        ref (GraphMat).

    Returns:
        str: String storing dot format of graph.

    """

    # Check if empty graph.
    if ref is None:
        return "graph G { }"
    # Build dot for non-empty graph.
    (s, link) = ("digraph", " -> ") if ref.directed else ("graph", " -- ")
    s += " G {\n"
    s += "node [shape = circle]\n"
    for src in range(ref.order):
        for dst in range(ref.order):
            if ref.directed or src >= dst:
                for i in range(ref.adj[src][dst]):
                    s += "  " + str(src) + link + str(dst) + '\n'
    s += '}'
    return s


def displaySVG(ref, filename='temp'):
    """Render a graph to SVG format.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (GraphMat).
        filename (str): Temporary filename to store SVG output.

    Returns:
        SVG: IPython SVG wrapper object for graph.

    """

    # Ensure all modules are available
    try:
        from graphviz import Graph as gvGraph, Digraph as gvDigraph
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse graph and generate temporary Digraph/Graph object
    output_format = 'svg'
    if ref.directed:
        graph = gvDigraph(filename, format=output_format)
    else:
        graph = gvGraph(filename, format=output_format)
    if ref is not None:
        for src in range(ref.order):
            src_id = 'node_' + str(src)
            graph.node(src_id, label=str(src))
            for dst in range(ref.order):
                if ref.adj[src][dst] > 0 and (ref.directed or src >= dst):
                    graph.edge(src_id, 'node_' + str(dst))
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)


def display(ref, eng=None):
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    display(Source(todot(ref), engine = eng))


# load / save gra(wgra) format    

def loadgra(filename, multigraph=False):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist.

    """

    with open(filename) as f:
        directed = bool(int(f.readline()))
        order = int(f.readline())
        g = GraphMat(order, directed)
        for line in f.readlines():
            edge = line.strip().split(' ')
            (src, dst) = (int(edge[0]), int(edge[1]))
            g.addedge(src, dst, multi=multigraph)
        return g

def savegra(G, fileOut):
    gra = str(int(G.directed)) + '\n'
    gra += str(G.order) + '\n'
    for s in range(G.order):
        n = G.order if G.directed else s
        for adj in range(n):    
            for i in range(G.adj[s][adj]):
                gra += str(s) + " " + str(adj) + '\n'
    with open(fileOut, mode='w') as fout: 
        fout.write(gra)
# 
def fromlist(order, directed, edges):
    """Build a new graph from an int tuple list.

    Args:
        order (int): Order of graph.
        directed (bool): True if the graph is directed. False otherwise.
        edges (List[(int, int)]): Source/Destination tuple list.

    Returns:
        GraphMat: New graph.

    Raises:
        IndexError: If either order or edge extremity is invalid.

    """

    # Check order:
    if order <= 0:
        raise IndexError('Invalid order')
    # Build graph
    g = GraphMat(order, directed)
    for (src, dst) in edges:
        g.adj[src][dst] += 1
        if not g.directed and src != dst:
            g.adj[dst][src] += 1
    return g


