import sys, getopt
import random

def main(argv):
	vertices = 1000
	degree = 10
	filename = 'synth-r'
   	try:
  		opts, args = getopt.getopt(argv,"v:d:c:f:")
   	except getopt.GetoptError:
      		print 'test.py -v <vertices> -d <degree> -f <filename>'
      		print 'test.py -v 100 -d 10 -f synth_r'
      		sys.exit(2)
   	for opt, arg in opts:
		if opt == '-e':
			edges = int(arg)
		elif opt == "-v":
			vertices = int(arg)
		elif opt == "-d":
			degree = int(arg)
		elif opt == "-f":
		 	filename = arg      
   	create_graph(vertices, degree, filename)

def create_graph(vertices, degree, filename):
	fnodes = open(filename+'.nodes.csv', 'w')
	fedges = open(filename+'.edges.csv', 'w')
	nodes=range(vertices)
	for i in nodes:
		fnodes.write(str(i)+'\n')
		for j in range(degree):
			while True:
				neighbor = random.randint(0,len(nodes)-1)
				if neighbor != i:
					break
			print i, nodes[neighbor]
			fedges.write( str(j)+","+ str(nodes[neighbor])+'\n')

if __name__ == "__main__":
   main(sys.argv[1:])
