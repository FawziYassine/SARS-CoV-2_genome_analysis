
def build_De_Bruijn_graph(str, k):
	"Builds a De Bruijn graph."
	edges = [] 
	nodes = set()

	for i in range(len(str) - k + 1): # loop through every k-mer in the string
		edges.append((str[i:i+k-1], str[i+1:i+k])) 
		nodes.add(str[i:i+k-1]) 
		nodes.add(str[i+1:i+k])

	return edges, nodes

# test1
edges, nodes = build_De_Bruijn_graph('AGCTACCACCACCGTCCAGTAGCT', 4)
print("De_Bruijn_graph of \'AGCTACCACCACCGTCCAGTAGCT\' has the following:")
print("edges:\n%s" % edges)
print("nodes:\n%s" % nodes)

def visualize_De_Bruijn_graph(str, k):
	"visualize a De Bruijn graph using graphviz."
	edges, nodes = build_De_Bruijn_graph(str, k)
	dot_str = 'digraph DeBruijn graph {\n'
	for node in nodes:
		dot_str += '  %s [label="%s"] ;\n' % (node, node)
	for src, dst in edges:
		dot_str += '  %s -> %s ;\n' % (src, dst)
	dot_str + '}\n'

# test 2
import gvmagic
visualize_De_Bruijn_graph('AGCTACCACCACCGTCCAGTAGCT', 4)


