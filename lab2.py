import sys

import numpy as np

def linearKernel(vec1, vec2):
	try:	
		len(vec1) == len(vec1)
		return np.dot(vec1, vec2) + 1
	except:
		print("The length of the vectors you have entered is not equal")
		sys.exit(1)



def matrixP(data):
	N = len(data)
	P = np.zeros((N, N))
	for i in range(N):
		x = np.array(data[i][0], data[i][1])
		for j in range(N):
			y = np.array(data[j][0], data[j][1])
			P = data[i][2]*data[j][2]*linearKernel(x, y)
	return P


def q_G_h(N):
	q = -1*np.ones(N)
	G = np.diag(-1*np.ones(N))
	h = np.zeros(shape=(N,1))
	return (q, G, h)


def callqp(P, q, G, h):
	r = qp(matrix(P) , matrix(q) , matrix(G) , matrix(h))
	return (alpha = list(r["x"]))
   


# Example

x = [1, 2]
y = [0, -1]
print(linearKernel(x, y))
print(q_G_h(3))
callqp()






#if __name__ == "__main__":
 #   main()