import numpy, math

def linearKernel(vec1, vec2):
    z   = numpy.dot(vec1, vec2) + 1
    return(z)

def polyKernel(vec1, vec2, p):
    z   = numpy.dot(vec1, vec2) + 1
    return(numpy.power(z, p))

def radialKernel(vec1, vec2, sigma):
    diff = vec1 - vec2
    return(numpy.exp(-numpy.dot(diff,diff)/(2*sigma**2)) )

def sigmoidKernel(vec1, vec2, k, delta):
    return(numpy.tanh(numpy.dot(k*vec1,vec2) - delta))

def main():
    testArray   = numpy.array([1,2,3,4])
    out         = polyKernel(testArray, testArray,2)
    print(out)

if __name__ == '__main__':
    main()
