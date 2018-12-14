import numpy as np

# mech data import function : 
def readmeshdata(t_file):
	f = open(t_file)
	f.readline() # '$MeshFormat\n'
	f.readline() # '2.2 0 8\n'
	f.readline() # '$EndMeshFormat\n'
	f.readline() # '$Nodes\n'
	n_nodes = int(f.readline()) # '8\n'
	nodes = np.fromfile(f,count=n_nodes*4, sep=" ").reshape((n_nodes,4))
	f.readline() # '$EndNodes\n'
	f.readline() # '$Elements\n'
	n_elems = int(f.readline()) # '2\n'
	elems = np.fromfile(f,sep=" ")[:-1] 
	
	return n_elems

n_elems = readmeshdata("../TP1_gmsh/carre.msh")
print(n_elems)		
