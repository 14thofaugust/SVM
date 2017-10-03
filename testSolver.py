import lab2
def testSolver():
    mat = np.array(((2,3), (3,5)))
    print(mat)
    mat2= matrix(mat)
    print(mat2)
    P   = 2 * matrix([ [2, .5], [.5, 1] ])
    q   = matrix([1.0, 1.0])
    G   = matrix([[-1.0, 0.0],[0.0, -1.0]])
    h   = matrix([0.0, 0.0])

    A   = matrix([1.0, 1.0], (1,2))
    b   = matrix(1.0)
    alpha    = callqp(P, q, G, h)
    for val in alpha:
        print(val)
