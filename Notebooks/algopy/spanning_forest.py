# Spanning Forest visualization
# Requires graphviz

from graphviz import Digraph

spanning_colors = {'discovery': 'black', 'forward': 'blue', 'backward': 'red', 'cross': 'orange' }

class SpanningForest:

    def __init__(self, colors=spanning_colors, orders=False):
        self.__iner_tree = Digraph(node_attr={'shape': ('plain' if orders else 'oval')})
        self.__colors = colors
        self.__orders = orders


    def label(self, v, pre, post):
        self.__iner_tree.node(self._lab(v),
                label='< <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD COLSPAN="2">{}</TD></TR><TR><TD>{}</TD><TD>{}</TD></TR></TABLE> >'.format(v, pre, post))
        
    def discovery(self, src, dst):
        self.__iner_tree.edge(self._lab(src), self._lab(dst), color=self.__colors['discovery'])

    def forward(self, src, dst):
        self.__iner_tree.edge(self._lab(src), self._lab(dst), constraint='false', color=self.__colors['forward'])

    def backward(self, src, dst):
        self.__iner_tree.edge(self._lab(src), self._lab(dst), constraint='false', color=self.__colors['backward'])

    def cross(self, src, dst):
        self.__iner_tree.edge(self._lab(src), self._lab(dst), constraint='false', color=self.__colors['cross'])

    def _lab(self, v):
        return 'vert{}'.format(v) if self.__orders else str(v)

    def _repr_svg_(self):
        return self.__iner_tree._repr_svg_()

    def rank_roots(self, roots):
        for i in range(len(roots) - 1):
            self.__iner_tree.edge(self._lab(roots[i]), self._lab(roots[i + 1]),
                    style = 'invis', minlen='8')
        with self.__iner_tree.subgraph() as r:
            r.attr(rank='same')
            for v in roots:
                r.node(self._lab(v))

    def _display(self):
        '''Displays SVG representation directly in IPython notebook.

        Requires IPython and (through method _repr_svg_) graphviz modules.
        '''
        try:
            from IPython.display import display_svg
        except:
            raise Exception('Missing moduke: IPtyhon')
        display_svg(self)


    @property
    def source(self):
        return self.__iner_tree.source

def __dfs_dir(g, v, pre, post, tree, count):
    pre[v] = count
    count += 1
    for s in g.adjlists[v]:
        if pre[s] is None:
            tree.discovery(v, s)
            count = __dfs_dir(g, s, pre, post, tree, count)
        else:
            if post[s] is None:
                tree.backward(v, s)
            else:
                if pre[s] < pre[v]:
                    tree.cross(v, s)
                else:
                    tree.forward(v, s)
    post[v] = count
    return count + 1

def dfs_extra_edges_directed(g, v, order=False):
    tree = SpanningForest(orders=order)
    pre, post = [None] * g.order, [None] * g.order
    count = 0
    roots = [v]
    count = __dfs_dir(g, v, pre, post, tree, count)
    for v in range(g.order):
        if pre[v] is None:
            roots.append(v)
            count = __dfs_dir(g, v, pre, post, tree, count)
    tree.rank_roots(roots)
    if order:
        for v in range(g.order):
            tree.label(v, pre[v], post[v])
    return tree

def __dfs_undir(g, v, pre, parents, count, tree):
    count += 1
    pre[v] = count
    for s in g.adjlists[v]:
        if parents[s] is None:
            parents[s] = v
            tree.discovery(v, s)
            count = __dfs_undir(g, s, pre, parents, count, tree)
        else:
            if parents[v] != s and pre[s] < pre[v]:
                tree.backward(v, s)
    return count

def dfs_extra_edges_undirected(g, v):
    parents = [None] * g.order
    count = 0
    tree = SpanningForest()
    pre = [None] * g.order
    parents[v] = -1
    count = __dfs_undir(g, v, pre, parents, count, tree)
    for v in range(g.order):
        if parents[v] is None:
            parents[v] = -1
            count = __dfs_undir(g, v, pre, parents, count, tree)
    return tree
