import sys, getopt
import random

def main(argv):
	vertices = 1000
	clusters = 4
	degree = 10
	filename = 'synth-c'
   	try:
  		opts, args = getopt.getopt(argv,"v:d:c:f:")
   	except getopt.GetoptError:
      		print 'test.py -v <vertices> -d <degree> -c <clusters> -f <filename>'
      		print 'test.py -v 1000 -d 10 -c 4'
      		sys.exit(2)
   	for opt, arg in opts:
		if opt == '-e':
			edges = int(arg)
		elif opt == "-v":
			vertices = int(arg)
		elif opt == "-c":
		 	clusters = int(arg)
		elif opt == "-f":
		 	filename = arg      
   	create_graph(vertices, degree, clusters, filename)

def create_graph(vertices, degree, clusters, filename):
	nodes_per_cluster = (vertices/clusters)	
	fnodes = open(filename+'.nodes.csv', 'w')
	fedges = open(filename+'.edges.csv', 'w')
	nodes=range(vertices)
	for i in xrange(0,clusters):
		cluster_nodes = range(i*nodes_per_cluster,i*nodes_per_cluster+nodes_per_cluster)
		for j in cluster_nodes:
			fnodes.write(str(j)+'\n')
			count = 1
			for k in range(degree):
				if count < degree*0.75:
					while True:
						neighbor = random.randint(0,len(cluster_nodes)-1)
						if neighbor != j:
							break
					fedges.write( str(j)+","+ str(cluster_nodes[neighbor])+'\n')
				else:
					while True:
						neighbor = random.randint(0,len(nodes)-1)
						if neighbor != j:
							break
					fedges.write( str(j)+","+ str(nodes[neighbor])+'\n')
				count+=1

if __name__ == "__main__":
   main(sys.argv[1:])
