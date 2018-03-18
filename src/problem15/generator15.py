import random

def write_testcase(results, filename='test15.in'):
    """
    write testcases
    :param filename: filename
    :return: write testcases to file
    """
    lines = map(lambda result: ' '.join(map(lambda x: str(x), result)), results)
    f = open(filename, 'w')
    f.write(str(len(results)) + '\n')
    f.write('\n'.join(lines))
    f.close()

n_tests = 1000
testcases = [
    [1, 1, 4, 1, 1, 1, 4, 1],  # same line
    [1, 1, -999, 1, 1234, -999, 999, 4321], # some negative values
    [1, 1, 4, 1, 10, 10, 10, 20], # //Ox vs //Oy
    [1, 1, 100, 100, 210, 10, 410, 210], # // triangle
    [0, 0, 1, 10000, 0, 0, 2, 20001], # nearly //
    [0, 0, 100, 0, -10, 30, 200, 30], # // Oy
    [0, 0, 0, 100, -10, 30, -10, -200], # // Ox
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)], # some random values

]
write_testcase(testcases)