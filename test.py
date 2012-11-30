import sys, getopt
import random

def main(argv):
	vertices = 100
	edges =400
	clusters = 2
	filename = 'temp'
   	try:
  		opts, args = getopt.getopt(argv,"v:e:c:f:")
   	except getopt.GetoptError:
      		print 'test.py -v <vertices> -e <edges> -c <clusters> -f <filename>'
      		print 'test.py -v 100 -e 400 -c 2'
      		sys.exit(2)
   	for opt, arg in opts:
		if opt == '-e':
			edges = int(arg)
		elif opt == "-v":
			vertices = int(arg)
		elif opt == "-e":
			edges = int(arg)
		elif opt == "-c":
		 	clusters = int(arg)
		elif opt == "-f":
		 	filename = arg      
   	create_graph(vertices, edges, clusters, filename)

def create_graph(vertices, edges, clusters, filename):
	nodes_per_cluster = (vertices/clusters)
	degree_of_node = (edges/vertices)	
	fnodes = open(filename+'.nodes.csv', 'w')
	fedges = open(filename+'.edges.csv', 'w')
	all_nodes =[]
	for i in xrange(0,clusters):
		nodes=range(i*nodes_per_cluster,i*nodes_per_cluster+nodes_per_cluster)
		all_nodes+=nodes
		for j in nodes:
			fnodes.write(str(j)+'\n')
			for k in xrange(0,degree_of_node):
				while True:
					neighbor = random.randint(0,len(nodes)-1)
					if neighbor != j:
						break
				print j, nodes[neighbor]
				fedges.write( str(j)+","+ str(nodes[neighbor])+'\n')
	
	for i in range(edges*0.10):
		fedges.write( str(all_nodes[random.randint(0,len(all_nodes)-1)])+","+ str(all_nodes[random.randint(0,len(all_nodes)-1)])+'\n')

if __name__ == "__main__":
   main(sys.argv[1:])
