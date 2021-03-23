import networkx as nx
import networkx.algorithms.connectivity.stoerwagner
import datetime
import igraph as ig
import pandas
import sys

if __name__ == '__main__':
	G = nx.Graph()
	graph = ig.Graph()
	print(sys.argv)
	filenames = sys.argv[1:]
	for filename in filenames:
		f = open(filename, 'r')
		tuplist = []
		weights = []
		idx = 0
		for line in f.readlines():
			if(idx > 7):
				lines = line.split(" ")
				if((lines[1], lines[2]) not in tuplist and (lines[2], lines[1]) not in tuplist):
					if int(lines[3]) != 0:
						G.add_edge(lines[1], lines[2], weight=int(lines[3]))
						graph.add_vertex(lines[1])
						graph.add_vertex(lines[2])
						graph.add_edge(lines[1], lines[2], weight=int(lines[3]), capacity=int(lines[3]))
						tuplist.append((lines[1],lines[2])) 
						weights.append(int(lines[3]))

			idx += 1
		start = datetime.datetime.now()
		#G.remove_nodes_from(nx.isolates(G))
		ans = nx.stoer_wagner(G)
		print("File: ", filename)
		print("MinCut Val: ", ans[0])
		#print("Partition: ", ans[1])
		end = datetime.datetime.now()
		print("Networkx Time Elapsed: ", end - start)
		print("||||||||||||||||||||||||||||")
		start = datetime.datetime.now()
		to_delete = [v.index for v in graph.vs if v.degree() == 0]
		graph.delete_vertices(to_delete)
		mincut = graph.mincut(capacity=weights)
		print("MinCutVal: ", mincut.value)
		print("Partition: ", mincut.partition)
		end = datetime.datetime.now()
		print("Igraph Time Elapsed: ", end - start)
		print("============================")
		f.close()
