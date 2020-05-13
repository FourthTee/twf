import solver

def test1():

    potenStart = [1, 3]
    lst = [1, 0, 0, 0, 0, 0, 1, 1, 3]
    try:
        assert solver.solve(potenStart, lst) == 86
        print("Test 1 Pass")
    except AssertionError:
        print("Test 1 Fail: " + str(solver.solve(potenStart, lst)))

def test2():
    
    potenStart = [1, 3]
    lst = [1, 1, 1, 0, 0, 0, 1, 1, 1]
    try:
        assert solver.solve(potenStart, lst) == 118
        print("Test 2 Pass")
    except AssertionError:
        print("Test 2 Fail: "+ str(solver.solve(potenStart, lst)))

def test3():
    
    potenStart = [1]
    lst = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    try:
        assert solver.solve(potenStart, lst) == 78
        print("Test 3 Pass")
    except AssertionError:
        print("Test 3 Fail: "+ str(solver.solve(potenStart, lst)))

def test4():
    
    potenStart = [1, 2]
    lst = [1, 1, 1, 1, 0, 0, 0, 0, 0]
    try:
        assert solver.solve(potenStart, lst) == 168
        print("Test 4 Pass")
    except AssertionError:
        print("Test 4 Fail: "+ str(solver.solve(potenStart, lst)))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()