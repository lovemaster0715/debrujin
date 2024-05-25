import pydot
def debjujin (st, k):
    edges = []
    nodes  = set()
    for i in range (len (st) - k+1):
        edges.append ((st[i:i+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges

def graphr (st,k):
    nodes,edges = debjujin(st, k)
    dot_str = 'digraph "dbrurijn" {\n'
    for node in nodes:
        dot_str += ' %s [label= "%s"] ; \n' % (node, node)
    for src, dst in edges:
        dot_str += '%s -> "%s" ; \n' % (src, dst)
    return dot_str + '}\n'


g = grap(graphr('ATGGAAGTCGCGGAATC', 3))

