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
	alpha = list(r['x'])
	return alpha
   

def buildIndList(data, alpha, tol=0.00001):
    N = 0
    for i in range(len(data)):
        if alpha[i] > tol:
            N += 1
    print('Non zero alphas: ', N)

    indList = np.zeros((N,4))
    i = 0
    for j in range(len(data)):
        if alpha[j] > tol:
            indList[i][0] = data[j][0]
            indList[i][1] = data[j][1]
            indList[i][2] = data[j][2]
            indList[i][3] = alpha[j]
            i += 1
    return(indList)
    #ca retourne (x, y, t, alpha)

def indicator(x, y, indList):
    point = np.array((x,y))
    N = len(indList)
    ind_x = 0.0
    for i in range(N):
        x_i     = np.array((indList[i][0], indList[i][1]))
        ind_x   += indList[i][3]*indList[i][2]*linearKernel(point, x_i)
    #indication = 0.0
    #indication += -1.0*(ind_x <= -1.0) + 1.0*(1.0 <= ind_x)
    return (ind_x)



def generateTestData(dataPoints):
    classA =[(random.normalvariate(-1.5, 0.1),
                random.normalvariate(1.5, 0.1),
                1.0)
                for i in range(int(dataPoints/4))] + \
            [(  random.normalvariate(1.5, 0.1),
                random.normalvariate(-1.5, 0.1),
                1.0)
                for i in range(int(dataPoints/4))]

    classB =[(  random.normalvariate(0.0, 0.5),
                random.normalvariate(-0.5, 0.5),
                -1.0)
                for i in range(int(dataPoints/2))]
    data        = classA + classB
    random.shuffle(data)
    return(data, classA, classB)

def plotTestData(classA, classB):
    pylab.hold(True)
    pylab.plot( [p[0] for p in classA],
                [p[1] for p in classA],
                'bo')
    pylab.plot( [p[0] for p in classB],
                [p[1] for p in classB],
                'ro')
    #pylab.show()


def plotContour(indList, kernArg):
    xRange  = np.arange(-4,4,0.1)
    yRange  = np.arange(-4,4,0.1)
    grid    = matrix([[indicator(x,y, indList, kernArg)
                for y in yRange]
                for x in xRange])

    pylab.contour(xRange, yRange, grid,
                    (-1, 0, 1),
                    colors=('red', 'black', 'blue'),
                    linewidths=(1,3,1))
    pylab.show()


def addSlack(G, h, C, N):
    G_slack = np.diag(np.ones(N))
    h_slack = C * np.ones(shape=(N,1))
    G_full  = np.concatenate((G,G_slack), axis=0)
    h_full  = np.concatenate((h,h_slack), axis=0)
    return(G_full, h_full)


# Example







#if __name__ == "__main__":
 #   main()