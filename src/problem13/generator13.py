import random

def write_testcase(results, filename='test13.in'):
    """
    write testcases
    :param filename: filename
    :return: write testcases to file
    """
    f = open(filename, 'w')
    f.write(str(len(results)) + '\n')
    newline = False
    for result in results:
        if newline:
            f.write('\n')
        f.write(str(len(result)) + '\n')
        f.write('\n' .join([' '.join(map(str, arr)) for arr in result]))
        newline = True
    f.close()

n_tests = 20
testcases = []
for i in range(n_tests):
    n = i + 1
    testcase = []
    for j in range(n):
        testcase.append([random.randint(1, 1000) for k in range(max(int(random.gauss(5+i, 0.8*i)), 1))])
    testcases += [testcase]
write_testcase(testcases)